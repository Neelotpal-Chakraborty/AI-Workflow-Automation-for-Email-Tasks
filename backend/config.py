import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    # Database (Postgres)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:1234@localhost:5432/agentdb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # IMAP/SMTP
    IMAP_HOST = os.getenv("IMAP_HOST", "")
    IMAP_PORT = int(os.getenv("IMAP_PORT", "993"))
    IMAP_USER = os.getenv("IMAP_USER", "")
    IMAP_PASSWORD = os.getenv("IMAP_PASSWORD", "")
    IMAP_FOLDER = os.getenv("IMAP_FOLDER", "INBOX")

    SMTP_HOST = os.getenv("SMTP_HOST", "")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

    # LLM
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # default fallback

    # Scheduler
    POLL_INTERVAL_SECONDS = int(os.getenv("POLL_INTERVAL_SECONDS", "180"))
    MAX_EMAILS_PER_CYCLE = int(os.getenv("MAX_EMAILS_PER_CYCLE", "20"))

    # Optional integrations
    TRELLO_API_KEY = os.getenv("TRELLO_API_KEY", "")
    TRELLO_TOKEN = os.getenv("TRELLO_TOKEN", "")
    TRELLO_LIST_ID = os.getenv("TRELLO_LIST_ID", "")

    GCAL_CALENDAR_ID = os.getenv("GCAL_CALENDAR_ID", "")
