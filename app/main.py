from fastapi import FastAPI
from .routes import router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    print(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")
