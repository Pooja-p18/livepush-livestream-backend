from fastapi import FastAPI
from app.routes.livestream import router as livestream_router


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Twinn Livepush backend is running"
    }


app.include_router(livestream_router)