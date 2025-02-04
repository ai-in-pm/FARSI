"""Test cases for FARSI agents."""
import unittest
from unittest.mock import patch, MagicMock
import sys
import io

from agents import (
    AIAgent,
    ModeratorAgent,
    AlgorithmAgent,
    RecursiveSystemsAgent,
    SafetyAgent,
    ArchitectureAgent,
    HardwareAgent
)
from exceptions import ValidationError, AgentCommunicationError


class TestAIAgent(unittest.TestCase):
    """Test cases for the base AIAgent class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = AIAgent("Test Agent", "Test Role", "Test Expertise")
    
    def test_initialization(self):
        """Test agent initialization."""
        self.assertEqual(self.agent.name, "Test Agent")
        self.assertEqual(self.agent.role, "Test Role")
        self.assertEqual(self.agent.expertise, "Test Expertise")
    
    def test_initialization_validation(self):
        """Test validation during initialization."""
        with self.assertRaises(ValidationError):
            AIAgent("", "Role", "Expertise")
        with self.assertRaises(ValidationError):
            AIAgent("Name", "", "Expertise")
        with self.assertRaises(ValidationError):
            AIAgent("Name", "Role", "")
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_speak(self, mock_stdout):
        """Test agent speaking functionality."""
        test_message = "Test message"
        response_time = self.agent.speak(test_message, typing_speed=0)
        
        output = mock_stdout.getvalue()
        self.assertIn(test_message, output)
        self.assertIn(self.agent.name, output)
        self.assertIn(self.agent.role, output)
        self.assertIsInstance(response_time, float)
    
    def test_speak_validation(self):
        """Test validation during speak method."""
        with self.assertRaises(ValidationError):
            self.agent.speak("")
        with self.assertRaises(ValidationError):
            self.agent.speak(None)


class TestSpecializedAgents(unittest.TestCase):
    """Test cases for specialized agent classes."""
    
    def test_moderator_agent(self):
        """Test ModeratorAgent initialization."""
        agent = ModeratorAgent()
        self.assertEqual(agent.name, "Agent Zeta")
        self.assertIn("Moderator", agent.role)
    
    def test_algorithm_agent(self):
        """Test AlgorithmAgent initialization."""
        agent = AlgorithmAgent()
        self.assertEqual(agent.name, "Agent Alpha")
        self.assertIn("Algorithm", agent.role)
    
    def test_recursive_systems_agent(self):
        """Test RecursiveSystemsAgent initialization."""
        agent = RecursiveSystemsAgent()
        self.assertEqual(agent.name, "Agent Beta")
        self.assertIn("Recursive", agent.role)
    
    def test_safety_agent(self):
        """Test SafetyAgent initialization."""
        agent = SafetyAgent()
        self.assertEqual(agent.name, "Agent Gamma")
        self.assertIn("Safety", agent.role)
    
    def test_architecture_agent(self):
        """Test ArchitectureAgent initialization."""
        agent = ArchitectureAgent()
        self.assertEqual(agent.name, "Agent Delta")
        self.assertIn("Architecture", agent.role)
    
    def test_hardware_agent(self):
        """Test HardwareAgent initialization."""
        agent = HardwareAgent()
        self.assertEqual(agent.name, "Agent Epsilon")
        self.assertIn("Hardware", agent.role)


if __name__ == '__main__':
    unittest.main()
