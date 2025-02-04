"""Metrics collection and analysis for the FARSI simulation."""
import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import os

@dataclass
class AgentMetrics:
    """Metrics for individual agent performance."""
    agent_id: str
    messages_sent: int
    total_chars: int
    avg_message_length: float
    response_times: List[float]
    
    @property
    def avg_response_time(self) -> float:
        """Calculate average response time."""
        return sum(self.response_times) / len(self.response_times) if self.response_times else 0.0

class MetricsCollector:
    """Collects and analyzes simulation metrics."""
    
    def __init__(self):
        """Initialize metrics collector."""
        self.start_time = time.time()
        self.agent_metrics: Dict[str, AgentMetrics] = {}
        self.simulation_events: List[Dict[str, Any]] = []
        
    def record_message(self, agent_id: str, message: str, response_time: float):
        """
        Record metrics for a message from an agent.
        
        Args:
            agent_id: Identifier of the agent
            message: Content of the message
            response_time: Time taken to generate response
        """
        if agent_id not in self.agent_metrics:
            self.agent_metrics[agent_id] = AgentMetrics(
                agent_id=agent_id,
                messages_sent=0,
                total_chars=0,
                avg_message_length=0.0,
                response_times=[]
            )
            
        metrics = self.agent_metrics[agent_id]
        metrics.messages_sent += 1
        metrics.total_chars += len(message)
        metrics.avg_message_length = metrics.total_chars / metrics.messages_sent
        metrics.response_times.append(response_time)
        
        self.simulation_events.append({
            'timestamp': datetime.now().isoformat(),
            'agent_id': agent_id,
            'message_length': len(message),
            'response_time': response_time
        })
    
    def save_metrics(self, output_dir: str = 'metrics'):
        """
        Save metrics to JSON files.
        
        Args:
            output_dir: Directory to save metrics files
        """
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Save agent metrics
        agent_metrics_file = os.path.join(output_dir, f'agent_metrics_{timestamp}.json')
        with open(agent_metrics_file, 'w') as f:
            json.dump({
                agent_id: asdict(metrics)
                for agent_id, metrics in self.agent_metrics.items()
            }, f, indent=2)
        
        # Save simulation events
        events_file = os.path.join(output_dir, f'simulation_events_{timestamp}.json')
        with open(events_file, 'w') as f:
            json.dump(self.simulation_events, f, indent=2)
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get summary of simulation metrics.
        
        Returns:
            Dictionary containing summary metrics
        """
        total_duration = time.time() - self.start_time
        total_messages = sum(m.messages_sent for m in self.agent_metrics.values())
        total_chars = sum(m.total_chars for m in self.agent_metrics.values())
        
        return {
            'duration_seconds': total_duration,
            'total_messages': total_messages,
            'total_characters': total_chars,
            'messages_per_second': total_messages / total_duration if total_duration > 0 else 0,
            'agent_summaries': {
                agent_id: {
                    'messages_sent': metrics.messages_sent,
                    'avg_message_length': metrics.avg_message_length,
                    'avg_response_time': metrics.avg_response_time
                }
                for agent_id, metrics in self.agent_metrics.items()
            }
        }
