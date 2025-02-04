from .base_agent import AIAgent

class ModeratorAgent(AIAgent):
    """Agent specialized in coordinating discussions and synthesizing information."""
    def __init__(self):
        super().__init__(
            name="Agent Zeta",
            role="Moderator & Coordinator",
            expertise="Theoretical AI and Meta-Learning"
        )

class AlgorithmAgent(AIAgent):
    """Agent specialized in algorithm design and self-modification systems."""
    def __init__(self):
        super().__init__(
            name="Agent Alpha",
            role="Algorithm Design Expert",
            expertise="Self-Modification Systems"
        )

class RecursiveSystemsAgent(AIAgent):
    """Agent specialized in recursive improvement and intelligence explosion."""
    def __init__(self):
        super().__init__(
            name="Agent Beta",
            role="Recursive Systems Specialist",
            expertise="Intelligence Explosion"
        )

class SafetyAgent(AIAgent):
    """Agent specialized in AI safety and alignment."""
    def __init__(self):
        super().__init__(
            name="Agent Gamma",
            role="Safety Expert",
            expertise="AI Alignment and Risk Management"
        )

class ArchitectureAgent(AIAgent):
    """Agent specialized in seed architectures and system validation."""
    def __init__(self):
        super().__init__(
            name="Agent Delta",
            role="Architecture Researcher",
            expertise="Seed Architectures and Validation"
        )

class HardwareAgent(AIAgent):
    """Agent specialized in hardware strategies and integration."""
    def __init__(self):
        super().__init__(
            name="Agent Epsilon",
            role="Hardware Strategist",
            expertise="Hardware Integration"
        )
