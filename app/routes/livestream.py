from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LivestreamRequest(BaseModel):
    title: str
    description: str
    platform: str
    
@router.post("/livestream")
def create_livestream(request: LivestreamRequest):
    return {
        "message" : "Livestream request received",
        "title" : request.title,
        "description" : request.description,
        "platform" : request.platform
    }
