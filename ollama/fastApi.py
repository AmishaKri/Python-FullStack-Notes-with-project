from fastapi import FastAPI, Body
from ollama import Client
app = FastAPI()
client=Client(
    host="http://localhost:11434",
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(
    message: str=Body(..., description="The Message" )
):
    
    response=client.chat(model="mistral:latest", messages=[
        {"role": "user", "content": message}
    ])
    
    return {"response": response.message.content}