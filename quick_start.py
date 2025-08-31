#!/usr/bin/env python3
"""
Quick start script for RL Migration Optimizer package.
This script demonstrates how to use the package programmatically.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def quick_demo():
    """Run a quick demonstration of the RL Migration Optimizer."""
    
    try:
        from rl_migration_optimizer.optimizer import MockMigrationOptimizer
        
        print("🤖 RL Migration Optimizer - Quick Demo")
        print("=" * 50)
        
        # Initialize the optimizer
        optimizer = MockMigrationOptimizer()
        print("✅ Optimizer initialized successfully")
        
        # Get performance metrics
        metrics = optimizer.get_performance_metrics()
        print(f"📊 Performance Metrics:")
        print(f"   - Total Optimizations: {metrics['total_optimizations']}")
        print(f"   - Avg Quality Score: {metrics['avg_quality_score']:.3f}")
        print(f"   - Avg Processing Time: {metrics['avg_processing_time']:.1f} min")
        print(f"   - Success Probability: {metrics['avg_success_probability']:.1%}")
        
        # Simulate training
        print("\n🎯 Training RL Model...")
        training_results = optimizer.train_model(num_episodes=100)
        print(f"✅ Training completed!")
        print(f"   - Total Episodes: {training_results['training_results']['total_episodes']}")
        print(f"   - Success Rate: {training_results['training_results']['success_rate']:.1%}")
        print(f"   - Avg Reward: {training_results['training_results']['avg_reward']:.2f}")
        
        # Optimize a migration strategy
        print("\n🚀 Optimizing Migration Strategy...")
        table_info = {
            'name': 'demo_table',
            'size_mb': 1000,
            'schema_complexity': 0.6,
            'data_type': 'structured',
            'source_system': 'postgresql',
            'target_system': 'bigquery',
            'priority': 3
        }
        
        resource_constraints = {
            'cpu_utilization': 0.7,
            'memory_utilization': 0.8,
            'network_bandwidth': 0.9,
            'disk_io': 0.6,
            'concurrent_migrations': 2
        }
        
        strategy = optimizer.optimize_migration_strategy(
            table_info=table_info,
            current_quality=0.85,
            resource_constraints=resource_constraints
        )
        
        print("✅ Strategy optimized successfully!")
        print(f"   - Expected Quality: {strategy['expected_performance']['quality_score']:.1%}")
        print(f"   - Processing Time: {strategy['expected_performance']['processing_time_minutes']:.1f} min")
        print(f"   - Success Probability: {strategy['expected_performance']['success_probability']:.1%}")
        print(f"   - Risk Level: {strategy['risk_assessment']['risk_level']}")
        
        # Export strategy
        export_path = optimizer.export_strategy_report(strategy)
        print(f"\n📥 Strategy exported to: {export_path}")
        
        print("\n🎉 Demo completed successfully!")
        print("\nTo run the full Streamlit app:")
        print("   streamlit run src/rl_migration_optimizer/app.py")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're in the package directory and dependencies are installed.")
        print("Run: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("Check the package installation and try again.")

def run_streamlit_app():
    """Run the Streamlit app directly."""
    try:
        import subprocess
        import sys
        
        print("🚀 Starting Streamlit app...")
        print("The app will open in your browser at http://localhost:8501")
        print("Press Ctrl+C to stop the app")
        
        # Run the Streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "src/rl_migration_optimizer/app.py"
        ])
        
    except FileNotFoundError:
        print("❌ Streamlit not found. Install it with: pip install streamlit")
    except KeyboardInterrupt:
        print("\n👋 App stopped by user")
    except Exception as e:
        print(f"❌ Error running Streamlit app: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Run quick demo")
    print("2. Start Streamlit app")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        quick_demo()
    elif choice == "2":
        run_streamlit_app()
    elif choice == "3":
        print("👋 Goodbye!")
    else:
        print("❌ Invalid choice. Running demo...")
        quick_demo()
