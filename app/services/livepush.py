# app/services/livepush.py
import httpx

LIVEPUSH_API_URL = "https://octopus.livepush.io"
# Replace with your API key from Livepush Dashboard -> Developer Settings
API_KEY = "livepush_api_key_here"


def create_stream(name: str):
    url = f"{LIVEPUSH_API_URL}/streams"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {"name": name}

    response = httpx.post(url, headers=headers, json=data)
    return response.json()