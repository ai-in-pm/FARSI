"""Custom exceptions for the FARSI simulation."""

class FARSIError(Exception):
    """Base exception class for FARSI-related errors."""
    pass

class ConfigurationError(FARSIError):
    """Raised when there's an error in the configuration."""
    pass

class APIKeyError(ConfigurationError):
    """Raised when there's an issue with API keys."""
    pass

class AgentError(FARSIError):
    """Base class for agent-related errors."""
    pass

class AgentCommunicationError(AgentError):
    """Raised when there's an error in agent communication."""
    pass

class AgentInitializationError(AgentError):
    """Raised when there's an error initializing an agent."""
    pass

class ValidationError(FARSIError):
    """Raised when validation fails."""
    pass

class SimulationError(FARSIError):
    """Raised when there's an error in the simulation."""
    pass
