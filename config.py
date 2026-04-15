import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.datamission.com.br")
DOWNLOADS_DIR = os.getenv("DOWNLOADS_DIR", "downloads")
LOGS_DIR = os.getenv("LOGS_DIR", "logs")
DEFAULT_PROJECT_ID = os.getenv("DEFAULT_PROJECT_ID", "default_project")
METADATA_FILE = os.path.join(LOGS_DIR, "execution_metadata.jsonl")

# Ensure directories exist
os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Scheduler settings
JOB_INTERVAL_MINUTES = int(os.getenv("JOB_INTERVAL_MINUTES", "60"))
