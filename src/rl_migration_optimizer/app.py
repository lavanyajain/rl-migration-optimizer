"""
Main Streamlit application for RL Migration Optimizer.
"""

import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
from datetime import datetime, timedelta
import sys
import os
import logging
import warnings
warnings.filterwarnings('ignore')

import sys
import os

# Add the current directory to Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from .optimizer import MockMigrationOptimizer
except ImportError:
    try:
        from optimizer import MockMigrationOptimizer
    except ImportError:
        # Last resort - create a simple mock class
        class MockMigrationOptimizer:
            def __init__(self):
                self.optimization_history = []
            def train_model(self, num_episodes=500):
                return {'training_results': {'total_episodes': num_episodes}}
            def get_performance_metrics(self):
                return {'total_optimizations': 0}
            def optimize_migration_strategy(self, *args, **kwargs):
                return {'expected_performance': {'quality_score': 0.9}}
            def export_strategy_report(self, strategy):
                return "migration_strategy.json"

# Set page config
st.set_page_config(
    page_title="Spark Migration Advisor",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
    }
    .stButton > button {
        border-radius: 20px;
        font-weight: bold;
    }
    .success-box {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .warning-box {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .error-box {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def main():
    """Main Streamlit application."""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 Spark Migration Advisor</h1>
        <p>AI-Powered Database Migration Strategy Generator with Spark Configuration Recommendations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'rl_optimizer' not in st.session_state:
        st.session_state.rl_optimizer = MockMigrationOptimizer()
        st.session_state.optimization_history = []
        st.session_state.current_strategy = None
        st.session_state.training_status = 'not_started'
    
    # Sidebar for configuration
    with st.sidebar:
        st.markdown("### ⚙️ **Configuration**")
        
        # Model training section
        st.markdown("#### 🎯 **Model Training**")
        if st.button("🚀 Train RL Model", type="primary"):
            with st.spinner("Training RL model..."):
                try:
                    st.session_state.training_status = 'training'
                    results = st.session_state.rl_optimizer.train_model(num_episodes=500)
                    st.session_state.training_status = 'completed'
                    st.session_state.training_results = results
                    st.success("✅ Model training completed!")
                except Exception as e:
                    st.error(f"❌ Training failed: {e}")
                    st.session_state.training_status = 'failed'
        
        # Show training status
        if st.session_state.training_status == 'training':
            st.info("🔄 Model training in progress...")
        elif st.session_state.training_status == 'completed':
            st.success("✅ Model trained successfully")
        elif st.session_state.training_status == 'failed':
            st.error("❌ Training failed")
        
        # Performance metrics
        st.markdown("#### 📊 **System Status**")
        try:
            # Get current session metrics
            total_optimizations = len(st.session_state.optimization_history)
            current_strategy = st.session_state.current_strategy
            
            # Display meaningful metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Session Optimizations", total_optimizations)
            
            with col2:
                if current_strategy:
                    quality = current_strategy['expected_performance']['quality_score']
                    st.metric("Latest Quality", f"{quality:.1%}")
                else:
                    st.metric("Latest Quality", "N/A")
            
            with col3:
                if current_strategy:
                    time = current_strategy['expected_performance']['processing_time_minutes']
                    st.metric("Latest Time", f"{time:.1f} min")
                else:
                    st.metric("Latest Time", "N/A")
            
            with col4:
                if current_strategy:
                    risk = current_strategy['risk_assessment']['risk_level']
                    st.metric("Latest Risk", risk)
                else:
                    st.metric("Latest Risk", "N/A")
                    
        except Exception as e:
            st.error(f"Error loading metrics: {e}")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 **Migration Strategy Optimization**")
        
        # Table information input
        with st.expander("📝 **Table Information**", expanded=True):
            col1a, col1b = st.columns(2)
            
            with col1a:
                table_name = st.text_input("Table/Collection Name", value="users_table", help="Name of your data table, collection, or dataset")
                table_size = st.number_input("Data Size (MB)", min_value=1, max_value=1000000, value=2500, help="Total size of your data in MB")
                schema_complexity = st.slider("Schema Complexity", 0.0, 1.0, 0.7, 0.1, help="0.0 = Simple flat structure, 1.0 = Complex nested relationships")
                data_type = st.selectbox("Data Type", ["structured", "semi-structured", "unstructured", "mixed"], help="Structure of your data")
                source_system = st.selectbox("Source System", ["postgresql", "mysql", "oracle", "sqlserver", "mongodb", "cassandra", "redis", "elasticsearch", "csv", "json", "parquet", "avro", "other"], help="Where your data currently resides")
                target_system = st.selectbox("Target System", ["spark", "hive", "bigquery", "snowflake", "redshift", "databricks", "emr", "kubernetes", "local", "cloud", "hybrid", "other"], help="Where you want to migrate your data")
            
            with col1b:
                current_quality = st.slider("Current Data Quality", 0.0, 1.0, 0.85, 0.05, help="How clean and accurate is your current data")
                priority = st.selectbox("Migration Priority", [1, 2, 3, 4, 5], index=2, help="1 = Low priority, 5 = Critical business need")
                
                st.markdown("#### **Resource & Performance Constraints**")
                cpu_utilization = st.slider("Available CPU", 0.0, 1.0, 0.6, 0.1, help="0.0 = No CPU available, 1.0 = Full CPU access")
                memory_utilization = st.slider("Available Memory", 0.0, 1.0, 0.7, 0.1, help="0.0 = No memory available, 1.0 = Full memory access")
                network_bandwidth = st.slider("Network Speed", 0.0, 1.0, 0.8, 0.1, help="0.0 = Slow network, 1.0 = High-speed network")
                disk_io = st.slider("Storage Performance", 0.0, 1.0, 0.5, 0.1, help="0.0 = Slow storage, 1.0 = High-performance storage")
                concurrent_migrations = st.number_input("Parallel Jobs", min_value=1, max_value=50, value=2, help="How many migrations can run simultaneously")
        
        # Advanced Configuration Options
        with st.expander("🔧 **Advanced Configuration Options**", expanded=False):
            col_adv1, col_adv2 = st.columns(2)
            
            with col_adv1:
                st.markdown("#### **Data Characteristics**")
                data_volume = st.selectbox("Data Volume Pattern", ["small", "medium", "large", "massive"], help="Expected data growth pattern")
                update_frequency = st.selectbox("Update Frequency", ["batch", "near-real-time", "real-time", "streaming"], help="How often data changes")
                data_consistency = st.selectbox("Consistency Requirements", ["eventual", "strong", "weak", "mixed"], help="Data consistency needs")
                backup_requirements = st.selectbox("Backup Strategy", ["none", "basic", "comprehensive", "disaster-recovery"], help="Backup and recovery needs")
            
            with col_adv2:
                st.markdown("#### **Business Requirements**")
                compliance_needs = st.selectbox("Compliance", ["none", "gdpr", "hipaa", "sox", "pci", "other"], help="Regulatory compliance requirements")
                sla_requirements = st.selectbox("SLA Requirements", ["flexible", "standard", "strict", "critical"], help="Service level agreement needs")
                cost_constraints = st.selectbox("Cost Sensitivity", ["low", "medium", "high", "critical"], help="Budget constraints")
                team_expertise = st.selectbox("Team Expertise", ["beginner", "intermediate", "advanced", "expert"], help="Technical team skill level")
        
        # Optimize button
        if st.button("🎯 **Generate Migration Strategy**", type="primary", use_container_width=True):
            with st.spinner("Optimizing migration strategy..."):
                try:
                    # Prepare comprehensive configuration
                    migration_config = {
                        'basic_info': {
                            'name': table_name,
                            'size_mb': table_size,
                            'schema_complexity': schema_complexity,
                            'data_type': data_type,
                            'source_system': source_system,
                            'target_system': target_system,
                            'priority': priority
                        },
                        'data_characteristics': {
                            'volume_pattern': data_volume,
                            'update_frequency': update_frequency,
                            'consistency_requirements': data_consistency,
                            'backup_strategy': backup_requirements
                        },
                        'business_requirements': {
                            'compliance': compliance_needs,
                            'sla_requirements': sla_requirements,
                            'cost_constraints': cost_constraints,
                            'team_expertise': team_expertise
                        },
                        'resource_constraints': {
                            'cpu_utilization': cpu_utilization,
                            'memory_utilization': memory_utilization,
                            'network_bandwidth': network_bandwidth,
                            'disk_io': disk_io,
                            'concurrent_migrations': concurrent_migrations
                        }
                    }
                    
                    # Generate comprehensive migration strategy
                    strategy = st.session_state.rl_optimizer.optimize_migration_strategy(
                        table_info=migration_config['basic_info'],
                        current_quality=current_quality,
                        resource_constraints=migration_config['resource_constraints']
                    )
                    
                    st.session_state.current_strategy = strategy
                    st.session_state.optimization_history.append({
                        'timestamp': datetime.now().isoformat(),
                        'table_name': table_name,
                        'strategy': strategy
                    })
                    
                    st.success("✅ Migration strategy optimized successfully!")
                    
                except Exception as e:
                    st.error(f"❌ Optimization failed: {e}")
    
    with col2:
        st.markdown("### 📈 **Quick Stats**")
        
        # Show current strategy if available
        if st.session_state.current_strategy:
            strategy = st.session_state.current_strategy
            
            st.metric(
                "Expected Quality", 
                f"{strategy['expected_performance']['quality_score']:.1%}"
            )
            st.metric(
                "Processing Time", 
                f"{strategy['expected_performance']['processing_time_minutes']:.1f} min"
            )
            st.metric(
                "Success Probability", 
                f"{strategy['expected_performance']['success_probability']:.1%}"
            )
            st.metric(
                "Risk Level", 
                strategy['risk_assessment']['risk_level']
            )
            
            # Risk level indicator
            risk_level = strategy['risk_assessment']['risk_level']
            if risk_level == "LOW":
                st.success("🟢 Low Risk")
            elif risk_level == "MEDIUM":
                st.warning("🟡 Medium Risk")
            else:
                st.error("🔴 High Risk")
    
    # Display current strategy
    if st.session_state.current_strategy:
        st.markdown("---")
        st.markdown("### 🎯 **Optimized Migration Strategy**")
        
        strategy = st.session_state.current_strategy
        
        # Create tabs for different aspects
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Performance", "⚙️ Parameters", "⚠️ Risk Assessment", "📋 Recommendations"])
        
        with tab1:
            st.markdown("#### **Expected Performance Metrics**")
            
            # Performance metrics visualization
            perf_data = strategy['expected_performance']
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Quality Score", f"{perf_data['quality_score']:.1%}")
            with col2:
                st.metric("Processing Time", f"{perf_data['processing_time_minutes']:.1f} min")
            with col3:
                st.metric("Resource Usage", f"{perf_data['resource_usage']:.1%}")
            with col4:
                st.metric("Success Probability", f"{perf_data['success_probability']:.1%}")
            
            # Performance radar chart
            fig = go.Figure()
            
            categories = ['Quality', 'Speed', 'Efficiency', 'Success Rate']
            values = [
                perf_data['quality_score'],
                1 - (perf_data['processing_time_minutes'] / 60),  # Normalize time
                perf_data['resource_usage'],
                perf_data['success_probability']
            ]
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name='Performance Metrics',
                line_color='rgb(32, 201, 151)',
                fillcolor='rgba(32, 201, 151, 0.3)'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 1]
                    )),
                showlegend=False,
                title="Performance Radar Chart"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.markdown("#### **Optimized Action Parameters**")
            
            params = strategy['action_parameters']
            
            # Create a nice parameter display
            param_data = {
                'Parameter': [
                    'Batch Size', 'Parallel Workers', 'Compression Level',
                    'Validation Frequency', 'Retry Strategy', 'Resource Allocation',
                    'Checkpoint Frequency', 'Error Handling'
                ],
                'Value': [
                    str(params['batch_size']),
                    str(params['parallel_workers']),
                    str(params['compression_level']),
                    f"{params['validation_frequency']:.1%}",
                    ['Immediate', 'Exponential Backoff', 'Adaptive'][params['retry_strategy']],
                    f"{params['resource_allocation']:.1%}",
                    f"{params['checkpoint_frequency']:.1%}",
                    ['Skip', 'Retry', 'Abort'][params['error_handling']]
                ],
                'Description': [
                    'Records per batch',
                    'Number of parallel workers',
                    'Data compression level (0-9)',
                    'How often to validate data',
                    'Strategy for handling retries',
                    'Resource allocation percentage',
                    'How often to create checkpoints',
                    'Strategy for handling errors'
                ]
            }
            
            param_df = pd.DataFrame(param_data)
            st.dataframe(param_df, use_container_width=True, hide_index=True)
        
        with tab3:
            st.markdown("#### **Risk Assessment**")
            
            risk_data = strategy['risk_assessment']
            
            # Risk level with color coding
            risk_level = risk_data['risk_level']
            if risk_level == "LOW":
                st.success(f"🟢 **Risk Level: {risk_level}**")
            elif risk_level == "MEDIUM":
                st.warning(f"🟡 **Risk Level: {risk_level}**")
            else:
                st.error(f"🔴 **Risk Level: {risk_level}**")
            
            # Risk factors
            st.markdown("**Risk Factors:**")
            for factor in risk_data['risk_factors']:
                st.markdown(f"• {factor}")
            
            # Mitigation strategies
            st.markdown("**Mitigation Strategies:**")
            for mitigation_strategy in risk_data['mitigation_strategies']:
                st.markdown(f"• {mitigation_strategy}")
        
        with tab4:
            st.markdown("#### **Recommendations**")
            
            recommendations = strategy['recommendations']
            
            st.markdown(f"**Primary Strategy:** {recommendations['primary_strategy']}")
            
            st.markdown("**Fallback Strategy Parameters:**")
            fallback = recommendations['fallback_strategy']
            fallback_text = f"""
            - Batch Size: {fallback['batch_size']:,}
            - Parallel Workers: {fallback['parallel_workers']}
            - Compression Level: {fallback['compression_level']}
            - Validation Frequency: {fallback['validation_frequency']:.1%}
            - Resource Allocation: {fallback['resource_allocation']:.1%}
            """
            st.code(fallback_text)
            
            st.markdown("**Monitoring Points:**")
            for point in recommendations['monitoring_points']:
                st.markdown(f"• **{point['metric'].title()}**: {point['frequency']} - {point['threshold']}")
    
    # Session Summary and History
    st.markdown("---")
    
    # Session Summary
    if st.session_state.optimization_history:
        st.markdown("### 📊 **Session Summary**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Strategies Generated", len(st.session_state.optimization_history))
        
        with col2:
            if st.session_state.optimization_history:
                avg_quality = sum(
                    entry['strategy']['expected_performance']['quality_score'] 
                    for entry in st.session_state.optimization_history
                ) / len(st.session_state.optimization_history)
                st.metric("Average Quality Score", f"{avg_quality:.1%}")
            else:
                st.metric("Average Quality Score", "N/A")
        
        with col3:
            if st.session_state.optimization_history:
                risk_levels = [entry['strategy']['risk_assessment']['risk_level'] for entry in st.session_state.optimization_history]
                most_common_risk = max(set(risk_levels), key=risk_levels.count)
                st.metric("Most Common Risk Level", most_common_risk)
            else:
                st.metric("Most Common Risk Level", "N/A")
    
    # Optimization history
    if st.session_state.optimization_history:
        st.markdown("### 📚 **Optimization History**")
        
        # Create history dataframe
        history_data = []
        for entry in st.session_state.optimization_history:
            history_strategy = entry['strategy']
            history_data.append({
                'Timestamp': entry['timestamp'][:19],  # Remove timezone
                'Table': entry['table_name'],
                'Quality': f"{history_strategy['expected_performance']['quality_score']:.1%}",
                'Time (min)': f"{history_strategy['expected_performance']['processing_time_minutes']:.1f}",
                'Success Prob': f"{history_strategy['expected_performance']['success_probability']:.1%}",
                'Risk': history_strategy['risk_assessment']['risk_level']
            })
        
        history_df = pd.DataFrame(history_data)
        st.dataframe(history_df, use_container_width=True, hide_index=True)
        
        # Export button
        if st.button("📥 Export Strategy Report"):
            try:
                if st.session_state.current_strategy:
                    report_path = st.session_state.rl_optimizer.export_strategy_report(
                        st.session_state.current_strategy
                    )
                    st.success(f"✅ Strategy report exported to: {report_path}")
                    
                    # Download button
                    st.download_button(
                        label="📄 Download JSON Report",
                        data=json.dumps(st.session_state.current_strategy, indent=2),
                        file_name=f"migration_strategy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        mime="application/json"
                    )
            except Exception as e:
                st.error(f"❌ Export failed: {e}")
    
    # Training results visualization
    if hasattr(st.session_state, 'training_results') and st.session_state.training_results:
        st.markdown("---")
        st.markdown("### 🎓 **Model Training Results**")
        
        results = st.session_state.training_results
        training_results = results.get('training_results', {})
        
        if training_results:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Episodes", training_results.get('total_episodes', 0))
            with col2:
                st.metric("Success Rate", f"{training_results.get('success_rate', 0):.1%}")
            with col3:
                st.metric("Avg Reward", f"{training_results.get('avg_reward', 0):.2f}")
            with col4:
                st.metric("Avg Episode Length", f"{training_results.get('avg_episode_length', 0):.1f}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.8em;'>
        🚀 <strong>Spark Migration Advisor</strong> | 
        AI-Powered Database Migration Strategy Generator with Spark Configuration Recommendations
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
