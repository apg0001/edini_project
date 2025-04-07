import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Edini의 칭찬일기"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()