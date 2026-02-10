from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://carbon_fibre:johnwick@postgres:5432/lamina"

    class Config:
        env_file = ".env"


settings = Settings()
