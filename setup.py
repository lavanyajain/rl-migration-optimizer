#!/usr/bin/env python3
"""
Setup script for RL Migration Optimizer package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return "AI-Powered Database Migration Strategy Optimization using Reinforcement Learning"

# Read requirements
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(requirements_path):
        with open(requirements_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return [
        "streamlit>=1.32.0",
        "plotly>=5.18.0",
        "pandas>=2.2.0",
        "numpy>=1.26.0",
    ]

setup(
    name="rl-migration-optimizer",
    version="1.0.0",
    description="AI-Powered Database Migration Strategy Optimization using Reinforcement Learning",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Clean Sync Agent Team",
    author_email="admin@example.com",
    url="https://github.com/yourusername/rl-migration-optimizer",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "rl-migration-optimizer=rl_migration_optimizer.app:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="database migration reinforcement learning optimization ai ml",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/rl-migration-optimizer/issues",
        "Source": "https://github.com/yourusername/rl-migration-optimizer",
        "Documentation": "https://github.com/yourusername/rl-migration-optimizer#readme",
    },
    include_package_data=True,
    zip_safe=False,
)
