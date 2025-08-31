"""
RL Migration Optimizer Package

A standalone Streamlit application that provides AI-powered database migration 
strategy optimization using Reinforcement Learning concepts.
"""

__version__ = "1.0.0"
__author__ = "Clean Sync Agent Team"
__description__ = "AI-Powered Database Migration Strategy Optimization using RL"

from .app import main
from .optimizer import MockMigrationOptimizer

__all__ = ["main", "MockMigrationOptimizer"]
