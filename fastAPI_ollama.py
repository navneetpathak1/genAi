from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat

app = FastAPI()

# Request body schema
class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "FastAPI + Ollama is running 🚀"}


@app.post("/chat")
def chat_with_model(request: ChatRequest):
    try:
        response = chat(
            model='gemma3:270m',
            messages=[
                {"role": "user", "content": request.message}
            ],
        )

        return {
            "response": response.message.content
        }

    except Exception as e:
        return {"error": str(e)}
    



# uvicorn app:app --reload