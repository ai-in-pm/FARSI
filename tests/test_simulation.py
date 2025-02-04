"""Test cases for FARSI simulation."""
import unittest
from unittest.mock import patch, MagicMock
import os
import json

from farsi_simulation import FARSISimulation
from exceptions import ConfigurationError, SimulationError
from metrics import MetricsCollector


class TestFARSISimulation(unittest.TestCase):
    """Test cases for the FARSISimulation class."""
    
    @patch('config.validate_api_keys')
    def setUp(self, mock_validate):
        """Set up test fixtures."""
        mock_validate.return_value = True
        self.simulation = FARSISimulation()
    
    def test_initialization(self):
        """Test simulation initialization."""
        self.assertIsInstance(self.simulation.metrics, MetricsCollector)
        self.assertEqual(len(self.simulation.agents), 6)  # All agents initialized
        
        # Check all required agents exist
        required_agents = ['zeta', 'alpha', 'beta', 'gamma', 'delta', 'epsilon']
        for agent_id in required_agents:
            self.assertIn(agent_id, self.simulation.agents)
    
    @patch('config.validate_api_keys')
    def test_initialization_failure(self, mock_validate):
        """Test simulation initialization with invalid configuration."""
        mock_validate.return_value = False
        with self.assertRaises(ConfigurationError):
            FARSISimulation()
    
    @patch('agents.base_agent.AIAgent.speak')
    def test_agent_speak(self, mock_speak):
        """Test agent speaking functionality."""
        mock_speak.return_value = 1.0  # Mock response time
        
        test_message = "Test message"
        self.simulation._agent_speak('zeta', test_message)
        
        mock_speak.assert_called_once_with(test_message)
    
    @patch('agents.base_agent.AIAgent.speak')
    def test_run_demonstration(self, mock_speak):
        """Test running the complete demonstration."""
        mock_speak.return_value = 1.0  # Mock response time
        
        # Run demonstration
        self.simulation.run_demonstration()
        
        # Verify each agent spoke
        self.assertEqual(mock_speak.call_count, 7)  # All agents + conclusion
        
        # Check metrics were saved
        self.assertTrue(os.path.exists('metrics'))
        metric_files = os.listdir('metrics')
        self.assertTrue(any(f.startswith('agent_metrics_') for f in metric_files))
        self.assertTrue(any(f.startswith('simulation_events_') for f in metric_files))
        
        # Verify metrics content
        latest_metrics = max(
            [f for f in metric_files if f.startswith('agent_metrics_')],
            key=lambda x: os.path.getctime(os.path.join('metrics', x))
        )
        with open(os.path.join('metrics', latest_metrics)) as f:
            metrics_data = json.load(f)
            self.assertEqual(len(metrics_data), 6)  # All agents have metrics
    
    def test_error_handling(self):
        """Test error handling during simulation."""
        with patch('agents.base_agent.AIAgent.speak') as mock_speak:
            mock_speak.side_effect = Exception("Test error")
            
            with self.assertRaises(SimulationError):
                self.simulation._agent_speak('zeta', "Test message")


if __name__ == '__main__':
    unittest.main()
