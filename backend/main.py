from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from sqlalchemy import create_engine
import redis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})

redis_url = os.getenv("REDIS_URL")
r = redis.from_url(redis_url, decode_responses=True)

@app.get("/")
def read_root():
    r.set("status", "Cloud Redis working!")
    return {"message": r.get("status")}
