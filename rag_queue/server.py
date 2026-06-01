from fastapi import FastAPI, HTTPException, Query
from client.rqClient import queue
from queue.worker import process_query
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

@app.get("/")
async def hello():
    return {"message": "server is running"}

@app.post("/chat")
def chat(query: str = Query(..., description="The Message")):
    job = queue.enqueue(process_query, query)
    return {"status": "queued", "job_id": job.id}

@app.get("/job-status")
def get_result(job_id: str = Query(..., description="Job ID")):
    job = queue.fetch_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        "job_id": job.id,
        "status": job.status,
        "result": job.return_value,
    } 