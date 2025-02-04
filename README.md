# Fully Autonomous Recursive Self-Improvement (FARSI) Simulation

A sophisticated simulation demonstrating the concept of Fully Autonomous Recursive Self-Improvement (FARSI) through an interactive multi-agent discussion system with comprehensive logging, metrics collection, and error handling.

## Project Overview

This project simulates a panel discussion between six AI agents, each with PhD-level expertise in different aspects of FARSI. The simulation demonstrates real-time interaction with simulated typing effects to create an engaging and educational experience, while providing robust logging, metrics collection, and error handling capabilities.

## Features

### Core Features
- Multi-agent simulation system with specialized agent roles
- Real-time typing effect for natural conversation flow
- Environment-based API key management
- Modular agent architecture
- Interactive discussion flow

### Advanced Features
- **Comprehensive Logging System**
  - Timestamped log files
  - Different log levels (DEBUG, INFO, ERROR)
  - Console and file logging
  - Detailed operation tracking

- **Metrics Collection**
  - Message statistics tracking
  - Response time measurements
  - Character count analytics
  - JSON-based metrics storage

- **Error Handling**
  - Custom exception hierarchy
  - Graceful error recovery
  - Detailed error reporting
  - Proper error propagation

- **Testing Framework**
  - Comprehensive unit tests
  - Mock object support
  - Error case coverage
  - Automated test suite

## Project Structure

```
FARSI/
├── .env                    # API keys and configuration
├── agents/                 # Agent-specific implementations
│   ├── __init__.py        # Module initialization
│   ├── base_agent.py      # Base agent implementation
│   └── specialized_agents.py  # Specialized agent classes
├── config.py              # Configuration settings
├── exceptions.py          # Custom exceptions
├── farsi_simulation.py    # Main simulation orchestrator
├── logger.py              # Logging configuration
├── metrics/               # Metrics output directory
├── logs/                  # Log file directory
├── metrics.py             # Metrics collection
├── requirements.txt       # Project dependencies
├── tests/                 # Test suite
│   ├── __init__.py       # Test module initialization
│   ├── test_agents.py    # Agent tests
│   └── test_simulation.py # Simulation tests
├── utils.py              # Utility functions
└── README.md             # Project documentation
```

## Agents

1. **Agent Zeta (Moderator & Coordinator)**
   - Expertise: Theoretical AI and Meta-Learning
   - Role: Overall discussion coordination and synthesis
   - API Provider: Anthropic

2. **Agent Alpha (Algorithm Design Expert)**
   - Expertise: Self-Modification Systems
   - Role: Explains algorithmic aspects of self-improvement
   - API Provider: OpenAI

3. **Agent Beta (Recursive Systems Specialist)**
   - Expertise: Intelligence Explosion
   - Role: Discusses recursive improvement cycles
   - API Provider: Groq

4. **Agent Gamma (Safety Expert)**
   - Expertise: AI Alignment and Risk Management
   - Role: Addresses safety implications and controls
   - API Provider: Google

5. **Agent Delta (Architecture Researcher)**
   - Expertise: Seed Architectures and Validation
   - Role: Explains foundational system design
   - API Provider: Cohere

6. **Agent Epsilon (Hardware Strategist)**
   - Expertise: Hardware Integration
   - Role: Discusses hardware optimization strategies
   - API Provider: EmergenceAI

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source .venv/bin/activate
     ```

3. Install the project in development mode:
   ```bash
   pip install -e .
   ```

4. Configure environment variables:
   Create a `.env` file with the following API keys:
   ```
   OPENAI_API_KEY=your_key_here
   ANTHROPIC_API_KEY=your_key_here
   GROQ_API_KEY=your_key_here
   GOOGLE_API_KEY=your_key_here
   COHERE_API_KEY=your_key_here
   EMERGENCEAI_API_KEY=your_key_here
   ```

## Running the Simulation

1. Run the main simulation:
   ```bash
   python farsi_simulation.py
   ```

2. Run the test suite:
   ```bash
   python -m unittest discover tests
   ```

## Metrics and Logging

### Metrics Collection
The simulation automatically collects various metrics:
- Message counts per agent
- Response times
- Character counts
- Overall simulation duration

Metrics are saved in the `metrics/` directory as JSON files:
- `agent_metrics_[timestamp].json`: Per-agent statistics
- `simulation_events_[timestamp].json`: Timeline of events

### Logging System
Comprehensive logging is provided:
- Log files are stored in `logs/` directory
- Console output shows INFO level and above
- Log files contain all DEBUG level and above
- Timestamps and log levels are included

## Error Handling

The system includes a robust error handling framework:
- Custom exceptions for different error types
- Graceful error recovery where possible
- Detailed error messages and stack traces
- Proper error propagation through the system

## Development

### Running Tests
```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_agents
python -m unittest tests.test_simulation

# Run with verbosity
python -m unittest discover -v tests
```

### Adding New Agents
1. Create a new agent class in `agents/specialized_agents.py`
2. Inherit from `AIAgent` base class
3. Configure the agent in `config.py`
4. Add corresponding tests in `tests/test_agents.py`

### Extending Metrics
1. Add new metrics fields to `AgentMetrics` class in `metrics.py`
2. Update `MetricsCollector.record_message()` method
3. Modify `get_summary()` to include new metrics

## Security Note

The `.env` file contains sensitive API keys. Make sure to:
- Never commit the `.env` file to version control
- Keep your API keys secure and private
- Rotate keys regularly following security best practices
- Use appropriate file permissions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Update documentation
6. Submit a pull request

## License

This project is open source and available under the MIT License.
