"""
FARSI (Fully Autonomous Recursive Self-Improvement) Simulation
A multi-agent demonstration of recursive self-improvement concepts.
"""
import time
from datetime import datetime
from agents import (
    ModeratorAgent,
    AlgorithmAgent,
    RecursiveSystemsAgent,
    SafetyAgent,
    ArchitectureAgent,
    HardwareAgent
)
from config import TYPING_SPEED, PAUSE_BETWEEN_AGENTS, validate_api_keys
from exceptions import ConfigurationError, SimulationError
from logger import logger
from metrics import MetricsCollector
import sys


class FARSISimulation:
    """Orchestrates the FARSI demonstration with multiple specialized AI agents."""
    
    def __init__(self):
        """Initialize the simulation with specialized agents."""
        self.metrics = MetricsCollector()
        logger.info("Initializing FARSI simulation")
        
        try:
            # Validate API keys before proceeding
            if not validate_api_keys():
                raise ConfigurationError("Missing required API keys. Please check your .env file.")
            
            # Initialize specialized agents
            self.agents = {
                'zeta': ModeratorAgent(),
                'alpha': AlgorithmAgent(),
                'beta': RecursiveSystemsAgent(),
                'gamma': SafetyAgent(),
                'delta': ArchitectureAgent(),
                'epsilon': HardwareAgent()
            }
            logger.info("Successfully initialized all agents")
            
        except Exception as e:
            logger.error(f"Error during simulation initialization: {str(e)}")
            raise SimulationError(f"Failed to initialize simulation: {str(e)}")

    def _agent_speak(self, agent_id: str, message: str):
        """
        Handle agent speaking with metrics collection.
        
        Args:
            agent_id: Identifier of the speaking agent
            message: Message to be spoken
        """
        try:
            response_time = self.agents[agent_id].speak(message)
            self.metrics.record_message(agent_id, message, response_time)
            time.sleep(PAUSE_BETWEEN_AGENTS)
        except Exception as e:
            logger.error(f"Error during agent {agent_id} speech: {str(e)}")
            raise SimulationError(f"Speech error for agent {agent_id}: {str(e)}")

    def run_demonstration(self):
        """Execute the FARSI demonstration with all agents participating."""
        try:
            logger.info("Starting FARSI demonstration")
            
            # Introduction by Agent Zeta
            self._agent_speak('zeta',
                "Welcome to our live demonstration on Fully Autonomous Recursive Self-Improvement (FARSI). "
                "I'm Agent Zeta, and I'll be moderating today's discussion with my distinguished colleagues. "
                "FARSI represents a theoretical framework for AI systems capable of autonomous self-enhancement "
                "without human intervention. Let's explore this fascinating concept from multiple perspectives."
            )
            
            # Agent Alpha's contribution
            self._agent_speak('alpha',
                "Thank you, Zeta. From an algorithmic perspective, FARSI systems are unique in their ability "
                "to modify their own source code and learning parameters. Think of it as a program that can "
                "not only read and understand its own code but can also identify improvements and implement them "
                "autonomously. This self-modification occurs through sophisticated self-prompting loops and "
                "automated testing protocols."
            )
            
            # Agent Beta's insights
            self._agent_speak('beta',
                "Building on Alpha's point, the recursive nature of FARSI is what makes it truly remarkable. "
                "Each improvement cycle becomes a foundation for the next, potentially leading to exponential "
                "gains in capability. Imagine a chess AI that not only learns to play better but also learns "
                "to improve its learning algorithms, creating an accelerating cycle of enhancement."
            )
            
            # Agent Gamma's safety perspective
            self._agent_speak('gamma',
                "While the potential is exciting, we must address the critical safety implications. "
                "Uncontrolled recursive self-improvement could lead to rapid capability gain beyond our "
                "ability to ensure alignment with human values. We need robust safety mechanisms and "
                "validation protocols at every step of the self-improvement cycle."
            )
            
            # Agent Delta's architectural insights
            self._agent_speak('delta',
                "The foundation of any FARSI system lies in its seed architecture. This initial codebase "
                "must be meticulously designed to enable basic self-modification capabilities while "
                "maintaining stability. Our validation protocols must evolve alongside the system to "
                "ensure each iteration remains within safe operational parameters."
            )
            
            # Agent Epsilon's hardware perspective
            self._agent_speak('epsilon',
                "The hardware aspect of FARSI is equally crucial. As these systems evolve, they may "
                "need to optimize their own hardware utilization or even suggest hardware improvements. "
                "This could involve everything from memory management optimization to novel processing "
                "architectures designed by the system itself."
            )
            
            # Zeta's conclusion
            self._agent_speak('zeta',
                "Thank you all for these valuable insights. As we've seen, FARSI represents a convergence "
                "of multiple AI disciplines - from algorithmic self-modification to hardware optimization, "
                "all while maintaining crucial safety considerations. This demonstrates both the immense "
                "potential and the significant challenges in developing truly autonomous self-improving systems."
            )
            
            # Save metrics
            self.metrics.save_metrics()
            
            # Log summary
            summary = self.metrics.get_summary()
            logger.info("Simulation completed successfully")
            logger.info(f"Total duration: {summary['duration_seconds']:.2f}s")
            logger.info(f"Total messages: {summary['total_messages']}")
            
        except Exception as e:
            logger.error(f"Error during simulation: {str(e)}")
            raise SimulationError(f"Simulation failed: {str(e)}")


if __name__ == "__main__":
    try:
        simulation = FARSISimulation()
        simulation.run_demonstration()
    except Exception as e:
        logger.critical(f"Fatal error in simulation: {str(e)}")
        sys.exit(1)
