from fastapi import APIRouter


router = APIRouter(prefix="/test", tags=["test"])


@router.get("/")
async def getTest():
    return {"message": "Hello World meow"}
