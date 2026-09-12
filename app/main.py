from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Twinn Livepush backend is running"
    }
    
@app.post("/livestream")
def create_livestream():
    return {
        "message": "Livestream creation endpoint is working"
    }
