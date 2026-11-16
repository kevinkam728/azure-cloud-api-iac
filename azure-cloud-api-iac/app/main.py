import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/info")
async def info():
    environment = os.getenv("ENVIRONMENT", "local")
    return {"service": "cloud-api", "environment": environment}
