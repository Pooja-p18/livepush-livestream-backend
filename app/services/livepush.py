import httpx

LIVEPUSH_API_URL = "https://octopus.livepush.io"

def create_stream(access_token: str, name: str):
    
    url = f"{LIVEPUSH_API_URL}/streams"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type" : "application/json"
    }
    
    data = {
        "name" : name
    }
    
    response = httpx.post(
        url,
        headers = headers,
        json = data
    )
    
    
    return response.json()