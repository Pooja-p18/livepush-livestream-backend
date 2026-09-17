from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
import httpx

from app.config import (
    LIVEPUSH_CLIENT_ID,
    LIVEPUSH_CLIENT_SECRET,
    LIVEPUSH_REDIRECT_URI,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/login")
def login():
    params = {
        "client_id": LIVEPUSH_CLIENT_ID,
        "redirect_uri": LIVEPUSH_REDIRECT_URI,
        "response_type": "code",
        "scope": "streams.create",
    }
    authorization_url = f"https://id.livepush.io/oauth2/authorize?{urlencode(params)}"
    return RedirectResponse(url=authorization_url)


@router.get("/callback")
async def callback(code: str = Query(...)):
    token_url = "https://id.livepush.io/oauth2/token"

    payload = {
        "grant_type": "authorization_code",
        "client_id": LIVEPUSH_CLIENT_ID,
        "client_secret": LIVEPUSH_CLIENT_SECRET,
        "redirect_uri": LIVEPUSH_REDIRECT_URI,
        "code": code,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=payload)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Failed to fetch access token: {response.text}",
        )

    tokens = response.json()
    # tokens will contain {"access_token": "...", "refresh_token": "...", ...}
    return tokens