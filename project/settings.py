from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    PROJECT_NAME: str = "oauth"
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        env_file = ".env"


settings = Settings()
