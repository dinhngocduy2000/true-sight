from fastapi import FastAPI, Depends, HTTPException, Header, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from api.routers import test
app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


class NameRequest(BaseModel):
    name: str


@app.get("/")
async def getGreeting():
    return {"message": "Hello World meow"}


@app.post("/name",  status_code=status.HTTP_201_CREATED)
async def getName(request: NameRequest):
    try:
        return request

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=400,
            detail="Must not be a number"
        )

app.include_router(test.router)
