"""
Hydra + Environment configuration example from Chapter 8.

This demonstrates how to:
1. Combine Hydra's powerful features with environment-specific configs
2. Use Hydra's config groups for environment selection
3. Override configurations via command line
4. Load sensitive data from environment variables
"""

import os
import hydra
from omegaconf import DictConfig, OmegaConf
from dotenv import load_dotenv
from pathlib import Path


def setup_environment():
    """Load environment variables from .env file if it exists."""
    script_dir = Path(__file__).parent
    env_file = script_dir / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        print(f"✓ Loaded environment variables from {env_file}")


def enhance_config_with_secrets(config: DictConfig) -> DictConfig:
    """
    Enhance Hydra config with sensitive data from environment variables.
    
    Args:
        config: Hydra DictConfig object
        
    Returns:
        Enhanced configuration with secrets
    """
    # Create a mutable copy
    config_dict = OmegaConf.to_container(config, resolve=True)
    
    # Add database credentials if available
    if "database" in config_dict and os.getenv("DB_USER"):
        config_dict["database"]["user"] = os.getenv("DB_USER")
        config_dict["database"]["password"] = os.getenv("DB_PASSWORD", "")
    
    # Add API credentials
    config_dict.setdefault("secrets", {})
    
    env_secrets = {
        "aws_access_key": "AWS_ACCESS_KEY_ID",
        "aws_secret_key": "AWS_SECRET_ACCESS_KEY", 
        "alpha_vantage_key": "ALPHA_VANTAGE_KEY",
        "slack_webhook": "SLACK_WEBHOOK_URL",
        "sentry_dsn": "SENTRY_DSN"
    }
    
    for key, env_var in env_secrets.items():
        value = os.getenv(env_var)
        if value:
            config_dict["secrets"][key] = value
    
    # Override config values with environment variables
    if os.getenv("DEBUG_MODE"):
        if "processing" in config_dict:
            config_dict["processing"]["debug_mode"] = os.getenv("DEBUG_MODE").lower() == "true"
    
    if os.getenv("LOG_LEVEL"):
        config_dict["logging_level"] = os.getenv("LOG_LEVEL")
    
    # Convert back to DictConfig
    return OmegaConf.create(config_dict)


@hydra.main(config_path="config", config_name="development", version_base=None)
def process_with_environment_config(config: DictConfig):
    """
    Main processing function using Hydra with environment enhancements.
    
    Args:
        config: Hydra configuration object
    """
    # Setup environment variables
    setup_environment()
    
    # Enhance config with secrets
    enhanced_config = enhance_config_with_secrets(config)
    
    # Get environment name from config or command line override
    env_name = getattr(enhanced_config, 'environment', 'development')
    
    print("=" * 60)
    print(f"HYDRA + ENVIRONMENT DEMO ({env_name.upper()})")
    print("=" * 60)
    
    # Display configuration summary
    print_config_summary(enhanced_config)
    
    # Simulate data processing
    simulate_processing(enhanced_config)
    
    # Display Hydra-specific features
    demonstrate_hydra_features(enhanced_config)


def print_config_summary(config: DictConfig):
    """Print a summary of the loaded configuration."""
    
    print("\n📋 CONFIGURATION SUMMARY")
    print("-" * 30)
    
    print(f"Data source: {config.data_source}")
    print(f"Logging level: {config.logging_level}")
    
    if config.data_source == 'csv':
        print(f"File path: {config.file_path}")
    else:
        print(f"S3 bucket: {config.bucket}")
        print(f"S3 path: {config.file_path}")
    
    # Database info
    if 'database' in config:
        db = config.database
        print(f"Database: {db.type}")
        if hasattr(db, 'host'):
            print(f"Host: {db.host}:{db.port}")
        if hasattr(db, 'user'):
            print(f"User: {db.user}")
    
    # Processing settings
    if 'processing' in config:
        proc = config.processing
        print(f"Batch size: {proc.batch_size}")
        print(f"Workers: {proc.parallel_workers}")
        print(f"Debug mode: {proc.debug_mode}")
    
    # Secrets (show count only for security)
    if 'secrets' in config and config.secrets:
        secret_count = len(config.secrets)
        print(f"Secrets loaded: {secret_count} items")


def simulate_processing(config: DictConfig):
    """Simulate data processing with the loaded configuration."""
    
    print(f"\n🔄 PROCESSING SIMULATION")
    print("-" * 25)
    
    # Data loading
    if config.data_source == 'csv':
        print(f"📁 Loading from: {config.file_path}")
    else:
        print(f"☁️ Loading from S3: s3://{config.bucket}/{config.file_path}")
    
    # Feature processing
    if 'features' in config:
        print(f"📊 Processing {len(config.features)} features")
        if config.processing.debug_mode:
            print(f"   Features: {', '.join(config.features[:3])}...")
    
    # Model training simulation
    if 'model' in config:
        print(f"🤖 Training model (validation split: {config.model.validation_split})")
        print(f"💾 Saving to: {config.model.save_path}")
    
    # API interaction
    if 'api' in config:
        print(f"🌐 API endpoint: {config.api.base_url}")
        print(f"⏱️ Timeout: {config.api.timeout}s")
    
    print("✅ Processing completed!")


def demonstrate_hydra_features(config: DictConfig):
    """Demonstrate Hydra-specific features."""
    
    print(f"\n⚡ HYDRA FEATURES")
    print("-" * 20)
    
    # Show config access methods
    print("Config access examples:")
    print(f"  Dot notation: config.data_source = {config.data_source}")
    print(f"  Dict notation: config['logging_level'] = {config['logging_level']}")
    
    # Show interpolation example (if any)
    if 'model' in config and 'save_path' in config.model:
        print(f"  Model path: {config.model.save_path}")
    
    # Pretty print full config (excluding secrets)
    print(f"\n📄 FULL CONFIGURATION (excluding secrets):")
    config_copy = OmegaConf.create(OmegaConf.to_container(config, resolve=True))
    if 'secrets' in config_copy:
        config_copy.secrets = {"[HIDDEN]": f"{len(config.secrets)} items"}
    
    print(OmegaConf.to_yaml(config_copy, resolve=True))


if __name__ == "__main__":
    # This will be called by Hydra
    process_with_environment_config()