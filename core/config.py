from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Student Risk Prediction API"
    debug: bool = True

settings = Settings()