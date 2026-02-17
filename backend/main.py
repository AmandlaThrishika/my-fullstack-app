from fastapi import FastAPI
import redis
from sqlalchemy import create_engine

app = FastAPI()

# Redis connection
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# PostgreSQL connection
DATABASE_URL = "postgresql://postgres:Atreddy@1516@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    r.set("status", "Backend working!")
    return {"message": r.get("status")}
