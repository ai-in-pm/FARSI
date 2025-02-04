"""Utility functions for the FARSI simulation."""
import time
from typing import Optional, Callable
from functools import wraps


def with_typing_effect(func: Callable) -> Callable:
    """
    Decorator to add typing effect to text output.
    
    Args:
        func: The function to wrap with typing effect
    
    Returns:
        Wrapped function that displays text with typing effect
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            for char in result:
                print(char, end='', flush=True)
                time.sleep(0.02)
            print()
        return result
    return wrapper


def validate_message(message: Optional[str] = None) -> str:
    """
    Validate and clean message content.
    
    Args:
        message: Input message to validate
        
    Returns:
        Cleaned message string
        
    Raises:
        ValueError: If message is None or empty
    """
    if not message:
        raise ValueError("Message cannot be empty")
    return message.strip()


def format_timestamp() -> str:
    """
    Get formatted timestamp for logging.
    
    Returns:
        Formatted timestamp string
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")
