from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode

router = APIRouter()

CLIENT_ID = "18116004111680101103314"
REDIRECT_URI = "http://127.0.0.1:8000/auth/callback"

@router.get("/auth/login")
def login():

    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "streams.create",
    }

    authorization_url = (
        "https://id.livepush.io/oauth2/authorize?"
        + urlencode(params)
    )

    return RedirectResponse(url=authorization_url)