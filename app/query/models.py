from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class Citation(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    document_id: str
    document_title: str
    page_number: Optional[int]
    snippet: Optional[str]
    relevance_score: Optional[float]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class GeneratedResponse(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    query_id: str
    answer_text: str
    reasoning: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    citations: List[Citation] = []

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class SupportQuery(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    user_id: str
    question_text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    response: Optional[GeneratedResponse]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}