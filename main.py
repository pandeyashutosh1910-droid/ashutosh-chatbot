from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"status": "API is running"}


@app.post("/chat")
def chat(req: ChatRequest):

    user_msg = req.message.lower()

    print("Received:", user_msg)

    if "weather" in user_msg:
        reply = "Today's weather is sunny with moderate temperature."

    elif "hello" in user_msg or "hi" in user_msg:
        reply = "Hello! How can I help you?"

    elif "how are you" in user_msg:
        reply = "I'm just a chatbot, but I'm functioning perfectly!"

    elif "your name" in user_msg:
        reply = "I am your workshop AI assistant."

    else:
        reply = f"I heard you say: {req.message}"

    return {"reply": reply}
        


