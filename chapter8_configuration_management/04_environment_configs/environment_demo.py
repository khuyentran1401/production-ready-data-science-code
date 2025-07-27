"""
Environment-specific configuration management example from Chapter 8.

This demonstrates how to:
1. Load different configurations based on environment variables
2. Combine YAML configs with environment variables from .env files
3. Switch between development, staging, and production environments
4. Handle sensitive data securely
"""

import os
import yaml
from dotenv import load_dotenv
from pathlib import Path


def load_environment_config(environment: str = None) -> dict:
    """
    Load configuration for specified environment.
    
    Args:
        environment: Target environment (development, staging, production)
                    If None, reads from ENVIRONMENT env variable or defaults to development
    
    Returns:
        Configuration dictionary
    """
    # Get script directory for relative paths
    script_dir = Path(__file__).parent
    
    # Load environment variables from .env file if it exists
    env_file = script_dir / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        print(f"✓ Loaded environment variables from {env_file}")
    
    # Determine environment
    if environment is None:
        environment = os.getenv("ENVIRONMENT", "development")
    
    # Load environment-specific config
    config_file = script_dir / f"config/{environment}.yaml"
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_file}")
    
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
    
    # Enhance config with environment variables
    config = _enhance_with_env_vars(config)
    
    print(f"✓ Loaded {environment} configuration from {config_file}")
    return config


def _enhance_with_env_vars(config: dict) -> dict:
    """
    Enhance configuration with sensitive data from environment variables.
    """
    # Add database credentials if available
    if "database" in config:
        if os.getenv("DB_USER"):
            config["database"]["user"] = os.getenv("DB_USER")
        if os.getenv("DB_PASSWORD"):
            config["database"]["password"] = os.getenv("DB_PASSWORD")
    
    # Add API credentials if available
    config.setdefault("secrets", {})
    
    if os.getenv("AWS_ACCESS_KEY_ID"):
        config["secrets"]["aws_access_key"] = os.getenv("AWS_ACCESS_KEY_ID")
    if os.getenv("AWS_SECRET_ACCESS_KEY"):
        config["secrets"]["aws_secret_key"] = os.getenv("AWS_SECRET_ACCESS_KEY")
    if os.getenv("ALPHA_VANTAGE_KEY"):
        config["secrets"]["alpha_vantage_key"] = os.getenv("ALPHA_VANTAGE_KEY")
    
    # Override config values with environment variables if present
    if os.getenv("DEBUG_MODE"):
        config.setdefault("processing", {})["debug_mode"] = os.getenv("DEBUG_MODE").lower() == "true"
    
    if os.getenv("LOG_LEVEL"):
        config["logging_level"] = os.getenv("LOG_LEVEL")
    
    return config


def demonstrate_environment_switching():
    """Demonstrate switching between different environments."""
    
    environments = ["development", "staging", "production"]
    
    print("=" * 60)
    print("ENVIRONMENT CONFIGURATION DEMONSTRATION")
    print("=" * 60)
    
    for env in environments:
        print(f"\n📍 {env.upper()} ENVIRONMENT")
        print("-" * 40)
        
        try:
            config = load_environment_config(env)
            
            # Display key configuration details
            print(f"Data source: {config['data_source']}")
            print(f"Logging level: {config['logging_level']}")
            print(f"Database type: {config['database']['type']}")
            
            if config['data_source'] == 'csv':
                print(f"File path: {config['file_path']}")
            else:
                print(f"S3 bucket: {config['bucket']}")
                print(f"S3 path: {config['file_path']}")
            
            print(f"Batch size: {config['processing']['batch_size']}")
            print(f"Workers: {config['processing']['parallel_workers']}")
            print(f"Debug mode: {config['processing']['debug_mode']}")
            
            # Show secrets (without exposing actual values)
            if config.get("secrets"):
                print("Secrets loaded:")
                for key in config["secrets"]:
                    print(f"  - {key}: {'*' * 8}")
            
            # Show environment-specific features
            if env == "production":
                security = config.get("security", {})
                if security:
                    print("Security features:")
                    for key, value in security.items():
                        print(f"  - {key}: {value}")
            
        except Exception as e:
            print(f"❌ Error loading {env} config: {e}")


def simulate_data_processing(environment: str = None):
    """Simulate data processing with environment-specific settings."""
    
    config = load_environment_config(environment)
    env_name = environment or os.getenv("ENVIRONMENT", "development")
    
    print(f"\n🔄 SIMULATING DATA PROCESSING ({env_name.upper()})")
    print("-" * 50)
    
    # Simulate different data loading based on environment
    if config['data_source'] == 'csv':
        print(f"📁 Loading data from local file: {config['file_path']}")
    else:
        print(f"☁️ Loading data from S3: s3://{config['bucket']}/{config['file_path']}")
    
    # Simulate processing with environment-specific settings
    print(f"⚙️ Processing with {config['processing']['parallel_workers']} workers")
    print(f"📦 Batch size: {config['processing']['batch_size']}")
    
    if config['processing']['debug_mode']:
        print("🐛 Debug mode enabled - extra logging activated")
    
    # Simulate model saving
    print(f"💾 Saving model to: {config['model']['save_path']}")
    
    # Simulate monitoring (if available)
    if config.get('monitoring', {}).get('enabled'):
        print(f"📊 Sending metrics to: {config['monitoring']['metrics_endpoint']}")
    
    print("✅ Processing completed successfully!")


if __name__ == "__main__":
    # Demonstrate environment switching
    demonstrate_environment_switching()
    
    print("\n" + "=" * 60)
    print("PROCESSING SIMULATION")
    print("=" * 60)
    
    # Simulate processing in current environment
    simulate_data_processing()
    
    print(f"\n💡 TIP: Set ENVIRONMENT variable to switch configurations:")
    print("   export ENVIRONMENT=staging")
    print("   python environment_demo.py")