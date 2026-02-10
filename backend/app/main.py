from fastapi import FastAPI
from app.api.routers import health

app = FastAPI(title="Carbon Fibre")

app.include_router(health.router)
