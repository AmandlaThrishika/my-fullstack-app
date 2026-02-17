from fastapi import FastAPI
import os
from sqlalchemy import create_engine

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})

@app.get("/")
def read_root():
    return {"message": "Backend with cloud database working!"}

