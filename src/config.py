"""Project-wide constants: file paths, retrieval settings, model name."""

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Loads OPENAI_API_KEY (and optional overrides) from .env if the file exists.
load_dotenv(PROJECT_ROOT / ".env")

KNOWLEDGE_BASE_PATH = PROJECT_ROOT / "data" / "knowledge_base.json"
GOLDEN_DATASET_PATH = PROJECT_ROOT / "evals" / "golden_dataset.json"

TOP_K = 3

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
