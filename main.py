#!/usr/bin/env python3
"""
Main entry point for RL Migration Optimizer package.
This file can be run directly or imported as a module.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from rl_migration_optimizer.app import main

if __name__ == "__main__":
    main()
