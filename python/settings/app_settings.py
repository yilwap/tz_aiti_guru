from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    PROJECT_NAME: str = "tz_aiti_guru"
    VERSION: str = "1.0.0"

    class Config:
        case_sensitive = True


app_settings = AppSettings()
