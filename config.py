"""Configuration settings for the FARSI simulation."""
import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Simulation settings
TYPING_SPEED = 0.02  # seconds between characters
PAUSE_BETWEEN_AGENTS = 1.0  # seconds between agent messages

# API Configuration
API_KEYS: Dict[str, str] = {
    'OPENAI': os.getenv('OPENAI_API_KEY', ''),
    'ANTHROPIC': os.getenv('ANTHROPIC_API_KEY', ''),
    'GROQ': os.getenv('GROQ_API_KEY', ''),
    'GOOGLE': os.getenv('GOOGLE_API_KEY', ''),
    'COHERE': os.getenv('COHERE_API_KEY', ''),
    'EMERGENCEAI': os.getenv('EMERGENCEAI_API_KEY', '')
}

# Validate API keys
def validate_api_keys() -> bool:
    """Validate that all required API keys are present."""
    return all(API_KEYS.values())

# Agent configuration
AGENT_CONFIG: Dict[str, Dict[str, Any]] = {
    'zeta': {
        'class': 'ModeratorAgent',
        'api_provider': 'ANTHROPIC'
    },
    'alpha': {
        'class': 'AlgorithmAgent',
        'api_provider': 'OPENAI'
    },
    'beta': {
        'class': 'RecursiveSystemsAgent',
        'api_provider': 'GROQ'
    },
    'gamma': {
        'class': 'SafetyAgent',
        'api_provider': 'GOOGLE'
    },
    'delta': {
        'class': 'ArchitectureAgent',
        'api_provider': 'COHERE'
    },
    'epsilon': {
        'class': 'HardwareAgent',
        'api_provider': 'EMERGENCEAI'
    }
}
