from fastapi import FastAPI
from app.api.routers import auth, inspections, health

app = FastAPI(title="Carbon Fibre")

app.include_router(auth.router)
app.include_router(inspections.router)
app.include_router(health.router)