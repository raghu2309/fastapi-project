from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a request body model
class Message(BaseModel):
    text: str
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/message/")
def get_message(text: str):
    return {"response": f"You said: {text}"}

@app.post("/message/")
async def post_message(msg: Message):
    return {"response": f"You said: {msg.text}"}