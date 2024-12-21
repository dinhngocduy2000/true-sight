from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/")
async def getGreeting():
    return {"message": "Hello World meow"}


@app.get("/name/{name}")
async def getName(name: str):
    print(name)
    if name.isnumeric():
        raise HTTPException(
            status_code=400,
            detail="Must not be a number"
        )
    return {"name": name}
