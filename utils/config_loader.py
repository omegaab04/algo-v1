import json
import os
from dotenv import load_dotenv

def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def load_env():
    """Loads .env variables."""
    load_dotenv()