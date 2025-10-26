import os
import requests

class LLMModule:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY", "")
        self.base_url = os.getenv("LLM_API_URL", "https://api.openai.com/v1/chat/completions")

    def generate_response(self, prompt: str):
        if not self.api_key:
            raise ValueError("LLM API key not configured!")
        
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]}
        
        response = requests.post(self.base_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"LLM request failed: {response.status_code}, {response.text}")

# Singleton instance for app-wide use
llm_module = LLMModule()