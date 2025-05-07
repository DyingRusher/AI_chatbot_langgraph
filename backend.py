from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages:List[str]
    allow_search: bool

allowed_model = ["llama-3.3-70b-versatile",'llama3-8b-8192','mistral-saba-24b','gpt-4o-mini']

from fastapi import FastAPI

app = FastAPI(title="Ai chatbot langgraph")



@app.post("/chat")

def chat_endponint(request: RequestState):
    """
    API to chat with LLM
    """
    if request.model_name not in allowed_model:
        return {"error": "Model not allowed select other model"}
    
    llm_id = request.model_name
    llm_provider = request.model_provider
    system_prompt = request.system_prompt
    allow_search = request.allow_search
    query = request.messages

    response = get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,llm_provider)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=6969)