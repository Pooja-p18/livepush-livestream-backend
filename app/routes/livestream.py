from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from app.services.livepush import create_stream

router = APIRouter(tags=["Livestream"])


class LivestreamRequest(BaseModel):
    title: str
    description: str
    platform: str


@router.post("/livestream")
def create_livestream(
    request: LivestreamRequest,
    authorization: str = Header(...),  # Expecting 'Bearer <access_token>'
):
    token = authorization.replace("Bearer ", "")
    result = create_stream(access_token=token, name=request.title)
    return result