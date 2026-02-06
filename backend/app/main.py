from fastapi import FastAPI

app = FastAPI(title="Carbon Fibre")

@app.get("/health")
def health_check():
    return {"status": "healthy"}




#  Alembic .env configuration for async SQLAlchemy
# from app.infrastructure.db.session import Base
# from app.core.config import settings
# from sqlalchemy.ext.asyncio import create_async_engine

# config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# target_metadata = Base.metadata
