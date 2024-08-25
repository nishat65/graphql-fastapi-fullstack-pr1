from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URI: str
    DB: str
    PASSWORD: str
    USERNAME: str
    HOST: str
    PORT: str

    class Config:
        env_file = "./.env"


settings = Settings()
