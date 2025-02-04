"""Base agent implementation for the FARSI simulation."""
import sys
import time
from typing import Optional
from logger import logger
from exceptions import AgentCommunicationError, ValidationError
from utils import validate_message


class AIAgent:
    """Base class for AI agents in the FARSI simulation."""
    
    def __init__(self, name: str, role: str, expertise: str):
        """
        Initialize an AI agent.
        
        Args:
            name: The agent's identifier (e.g., 'Agent Alpha')
            role: The agent's role in the discussion
            expertise: The agent's area of expertise
            
        Raises:
            ValidationError: If any required field is empty
        """
        # Validate inputs
        if not all([name, role, expertise]):
            raise ValidationError("All agent fields (name, role, expertise) must be non-empty")
            
        self.name = name
        self.role = role
        self.expertise = expertise
        logger.info(f"Initialized {name} with role: {role}")
        
    def speak(self, message: str, typing_speed: Optional[float] = 0.02):
        """
        Display a message from the agent with a typing effect.
        
        Args:
            message: The text content to display
            typing_speed: Delay between characters for typing effect (seconds)
            
        Raises:
            AgentCommunicationError: If there's an error during message display
            ValidationError: If the message is empty
        """
        try:
            # Validate message
            message = validate_message(message)
            
            # Log the interaction
            logger.debug(f"{self.name} is preparing to speak: {message[:50]}...")
            
            start_time = time.time()
            
            # Display agent identifier
            print(f"\n[{self.name} - {self.role}]")
            
            # Simulate typing effect
            for char in message:
                try:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(typing_speed)
                except IOError as e:
                    raise AgentCommunicationError(f"Error during message display: {e}")
                    
            print("\n")
            
            # Calculate response time
            response_time = time.time() - start_time
            
            # Log completion
            logger.debug(f"{self.name} finished speaking. Response time: {response_time:.2f}s")
            
            return response_time
            
        except Exception as e:
            logger.error(f"Error in {self.name}'s speak method: {str(e)}")
            raise AgentCommunicationError(f"Communication error for {self.name}: {str(e)}")
            
    def __str__(self) -> str:
        """String representation of the agent."""
        return f"{self.name} ({self.role}) - Expert in {self.expertise}"
