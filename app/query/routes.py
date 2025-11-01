from fastapi import APIRouter, HTTPException
from app.infrastructure.database.mongo_client import database_module
from app.query.models import SupportQuery, GeneratedResponse, Citation
from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

router = APIRouter(prefix="/api/v1/query", tags=["Query"])
db = database_module.get_db()

if db:
    queries_collection = db["support_queries"]
    responses_collection = db["generated_responses"]
    citations_collection = db["citations"]
else:
    print("[Warning] No active MongoDB connection; using mock collections.")
    queries_collection = None
    responses_collection = None
    citations_collection = None

api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    openai_client = OpenAI(api_key=api_key)
else:
    print("[Warning] OPENAI_API_KEY not set; OpenAI client disabled.")
    openai_client = None


@router.post("/ask")
async def ask_question(question: dict):
    """Handles a user-submitted natural language question"""
    text = question.get("question")
    if not text:
        raise HTTPException(status_code=400, detail="Missing 'question' field")

    try:
        # Step 1: Generate embedding for question
        embedding_response = openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        query_embedding = embedding_response.data[0].embedding

        # Step 2: Vector search placeholder (no content indexed yet)
        relevant_chunks = []  # would come from a vector database (future)

        # Step 3: If no content, fallback message
        if not relevant_chunks:
            fallback_answer = (
                "I'm sorry, I don't have enough knowledge base content to answer that yet, "
                "but the system is learning more daily."
            )
            generated = GeneratedResponse(
                query_id="temp",
                answer_text=fallback_answer,
                reasoning=None,
                citations=[]
            )
        else:
            # Step 4: In the future, use retrieved context to prompt the LLM for grounded answer
            answer_prompt = f"Context: {relevant_chunks}\nQuestion: {text}\nProvide a cited answer."
            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": answer_prompt}]
            )
            answer_text = response.choices[0].message.content
            generated = GeneratedResponse(
                query_id="temp",
                answer_text=answer_text,
                reasoning="Generated based on retrieved context",
                citations=[]
            )

        # Step 5: Store SupportQuery and Response in MongoDB
        support_query = SupportQuery(
            user_id="test-user",
            question_text=text,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            response=generated
        )

        query_result = queries_collection.insert_one(support_query.dict(by_alias=True))
        support_query.id = str(query_result.inserted_id)
        generated.query_id = support_query.id
        responses_collection.insert_one(generated.dict(by_alias=True))

        return {"question": text, "answer": generated.answer_text, "status": "ok"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during RAG pipeline: {e}")