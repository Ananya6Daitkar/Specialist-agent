# Agent-Based Pricing System

## Overview

A lightweight agent-based pricing system that leverages Modal's serverless infrastructure to run remote AI models. This project demonstrates that effective agents don't require complex frameworks—just clean code and smart architecture.

## Components

### Agent (`Agent.py`)
Base class providing color-coded logging for observability across different agent types.

### Specialist Agent (`Specialist_agent.py`)
Connects to a Modal-hosted pricing model and provides price predictions for product descriptions. Core implementation is just two lines:
```python
def price(self, description: str) -> float:
    result = self.pricer.price.remote(description)
    return result
```

### Pricer Service (`pricer_service.py`)
Backend pricing service deployed on Modal's serverless infrastructure. Exposes a remote `price()` method for inference.

## Usage

```python
from Specialist_agent import SpecialistAgent

# Initialize agent
specialist = SpecialistAgent()

# Get price prediction
price = specialist.price("iPhone 14 Pro Max")
print(f"Predicted price: ${price}")
```

## Setup

```bash
# Install dependencies
pip install modal

# Configure Modal
modal token new

# Deploy the service
modal deploy pricer_service.py
```

## Technical Details

- **Platform**: Modal serverless AI infrastructure
- **Architecture**: Agent-based with remote model execution
- **Performance**: ~30s cold start, <1s warm execution
- **Design**: Minimal framework, maximum clarity
