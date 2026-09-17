from fastapi import FastAPI

from fastapi import FastAPI
from app.routes.livestream import router as livestream_router
from app.routes.auth import router as auth_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Twinn Livepush backend is running"}


app.include_router(livestream_router)
app.include_router(auth_router)