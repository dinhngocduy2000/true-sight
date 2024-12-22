from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


router = APIRouter(prefix="/test", tags=["test"])


class testResponse(BaseModel):
    message: str


@router.get("/", response_model=testResponse)
async def getTest():
    try:
        return {"message": "Hello World meow"}
    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="error")
