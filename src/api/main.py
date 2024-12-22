from fastapi import FastAPI, Depends, HTTPException, Header, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .database import Base, engine
from .routers import test, auth
app = FastAPI()
Base.metadata.create_all(bind=engine)
origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


class NameRequest(BaseModel):
    name: str


app.include_router(test.router)
app.include_router(auth.router)


@app.get("/")
async def getGreeting():
    return {"message": "Hello World meow"}
