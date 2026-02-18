import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    BASE_URL: str = os.getenv("BASE_URL", "")
    BROWSER: str = os.getenv("BROWSER", "chromium")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30000"))
    LOGIN: str = os.getenv("LOGIN", "")
    PASSWORD: str = os.getenv("PASSWORD", "")


settings = Settings()