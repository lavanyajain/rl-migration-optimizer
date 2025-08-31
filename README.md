# 🤖 RL Migration Optimizer Package

A professional Python package that provides AI-powered database migration strategy optimization using Reinforcement Learning concepts. This package is designed to be easily deployable on [Streamlit Cloud](https://share.streamlit.io/) and other hosting platforms.

## 🚀 Features

- **Migration Strategy Optimization**: Input table parameters and get AI-optimized migration strategies
- **Risk Assessment**: Comprehensive risk analysis with mitigation strategies
- **Performance Metrics**: Visual performance indicators and radar charts
- **Resource Management**: Optimize resource allocation and parallel processing
- **Export Functionality**: Download optimization reports in JSON format
- **Training Simulation**: Mock RL model training for demonstration purposes
- **Professional Package Structure**: Proper Python packaging with setup tools

## 📦 Package Structure

```
rl_migration_optimizer_package/
├── src/
│   └── rl_migration_optimizer/
│       ├── __init__.py          # Package initialization
│       ├── app.py               # Main Streamlit application
│       └── optimizer.py         # Mock RL optimizer implementation
├── tests/                       # Test files (to be added)
├── docs/                        # Documentation (to be added)
├── main.py                      # Main entry point
├── setup.py                     # Traditional setup script
├── pyproject.toml              # Modern Python packaging
├── requirements.txt             # Dependencies
└── README.md                   # This file
```

## 🛠️ Installation

### Option 1: Install from source

```bash
# Clone or download the package
cd rl_migration_optimizer_package

# Install in development mode
pip install -e .

# Or install normally
pip install .
```

### Option 2: Install dependencies only

```bash
cd rl_migration_optimizer_package
pip install -r requirements.txt
```

## 🏃‍♂️ Running the App

### Method 1: Using the package entry point

```bash
# After installation
rl-migration-optimizer

# Or
python -m rl_migration_optimizer.app
```

### Method 2: Direct execution

```bash
cd rl_migration_optimizer_package
python main.py

# Or
streamlit run src/rl_migration_optimizer/app.py
```

### Method 3: Import and run

```python
from rl_migration_optimizer.app import main
main()
```

## 🌐 Hosting on Streamlit Cloud

### Step 1: Prepare Your Repository

1. **Create a new GitHub repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: RL Migration Optimizer Package"
   git branch -M main
   git remote add origin https://github.com/yourusername/rl-migration-optimizer.git
   git push -u origin main
   ```

2. **Ensure your repository structure looks like this**:
   ```
   your-repo/
   ├── src/
   │   └── rl_migration_optimizer/
   │       ├── __init__.py
   │       ├── app.py
   │       └── optimizer.py
   ├── requirements.txt
   └── README.md
   ```

### Step 2: Deploy on Streamlit Cloud

1. **Go to [share.streamlit.io](https://share.streamlit.io/)**
2. **Sign in with your GitHub account**
3. **Click "New app"**
4. **Configure your app**:
   - **Repository**: Select your `rl-migration-optimizer` repository
   - **Branch**: Select `main`
   - **Main file path**: Enter `src/rl_migration_optimizer/app.py`
   - **App URL**: Choose a custom URL (optional)
5. **Click "Deploy!"**

### Step 3: Access Your App

Your app will be available at:
```
https://your-app-name.streamlit.app
```

## 🔧 Configuration

### Environment Variables

You can customize the app behavior using environment variables:

```bash
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
```

### Streamlit Configuration

Create a `.streamlit/config.toml` file in your repository:

```toml
[server]
headless = true
enableCORS = false
port = 8501

[browser]
gatherUsageStats = false
```

## 📊 Usage Guide

1. **Configure Parameters**: Set table information and resource constraints
2. **Train Model**: Click "Train RL Model" to simulate training
3. **Optimize Strategy**: Click "Optimize Migration Strategy" to generate recommendations
4. **Review Results**: Analyze performance metrics, risk assessment, and recommendations
5. **Export Report**: Download the optimization strategy as JSON

## 🧪 Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/yourusername/rl-migration-optimizer.git
cd rl-migration-optimizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

### Running tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=rl_migration_optimizer

# Run specific test file
pytest tests/test_optimizer.py
```

### Code formatting

```bash
# Format code with black
black src/

# Check code style with flake8
flake8 src/

# Type checking with mypy
mypy src/
```

## 🚨 Troubleshooting

### Common Issues

1. **Import errors**:
   ```bash
   # Make sure you're in the package directory
   cd rl_migration_optimizer_package
   
   # Install in development mode
   pip install -e .
   ```

2. **Streamlit not found**:
   ```bash
   pip install streamlit
   ```

3. **Port already in use**:
   ```bash
   streamlit run src/rl_migration_optimizer/app.py --server.port 8502
   ```

### Streamlit Cloud Issues

1. **App not deploying**: Check the main file path is correct (`src/rl_migration_optimizer/app.py`)
2. **Dependencies missing**: Ensure all dependencies are in `requirements.txt`
3. **Import errors**: Make sure the package structure is correct

## 🔮 Future Enhancements

- **Real RL Model Integration**: Connect to actual trained models
- **Database Connectivity**: Direct database schema analysis
- **Real-time Monitoring**: Live migration progress tracking
- **Multi-objective Optimization**: Balance quality, speed, and cost
- **API Endpoints**: RESTful API for programmatic access
- **Unit Tests**: Comprehensive test coverage
- **CI/CD Pipeline**: Automated testing and deployment

## 📚 API Reference

### MockMigrationOptimizer

The main class that provides migration optimization functionality.

#### Methods

- `train_model(num_episodes: int)`: Simulates RL model training
- `get_performance_metrics()`: Returns performance metrics
- `optimize_migration_strategy(table_info, current_quality, resource_constraints)`: Generates optimization strategy
- `export_strategy_report(strategy)`: Exports strategy to file

### Main App Function

- `main()`: Main Streamlit application entry point

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Inspired by reinforcement learning concepts
- Part of the Clean Sync Agent project

---

**Happy Optimizing! 🚀**

For questions or support, please open an issue in the repository or contact the development team.
