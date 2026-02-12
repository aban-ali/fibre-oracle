from fastapi import FastAPI
from app.api.routers import auth

app = FastAPI(title="Carbon Fibre")

app.include_router(auth.router)
