import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

# Agent Configuration
AGENT_MODEL = "deepseek/deepseek-chat"  # Free model for agent brain
MAX_ITERATIONS = 50
DEFAULT_TARGET_MODEL = "anthropic/claude-3.5-sonnet"

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./lupin.db")

# OpenRouter
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
