from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DATABASE: str

    class Config:
        env_prefix = "POSTGRES_"
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


db_settings = DBSettings()
