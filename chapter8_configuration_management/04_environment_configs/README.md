# Environment-Specific Configuration Management

This example demonstrates advanced configuration management techniques from Chapter 8, focusing on environment-specific configurations and secure handling of sensitive data.

## Features Demonstrated

- ✅ **Environment-specific config files** (development, staging, production)
- ✅ **Secure `.env` file management** with python-dotenv
- ✅ **Environment variable integration** with YAML configs
- ✅ **Hydra integration** with environment configs
- ✅ **Command-line environment switching**
- ✅ **Best practices for sensitive data handling**

## Quick Start

```bash
# From project root
cd chapter8_configuration_management/04_environment_configs

# Basic environment demo
uv run --group chapter8 python environment_demo.py

# Hydra-integrated demo (development environment)
uv run --group chapter8 python hydra_environment_demo.py

# Switch to staging environment
ENVIRONMENT=staging uv run --group chapter8 python environment_demo.py

# Switch to production environment  
ENVIRONMENT=production uv run --group chapter8 python environment_demo.py
```

## Environment Configuration Files

### Development (`config/development.yaml`)
- Local CSV files for data
- SQLite database
- Debug mode enabled
- Detailed logging (DEBUG level)
- Single worker for easy debugging

### Staging (`config/staging.yaml`) 
- S3 storage for data
- PostgreSQL database
- Medium-scale processing
- INFO level logging
- Basic monitoring enabled

### Production (`config/production.yaml`)
- S3 storage with production buckets
- PostgreSQL with SSL
- High-performance settings
- WARNING level logging only
- Full monitoring and security features

## Environment Variables (.env file)

Create a `.env` file from the example:

```bash
cp .env.example .env
# Edit .env with your actual credentials
```

Example `.env` content:
```bash
# Database credentials
DB_USER=myuser
DB_PASSWORD=mypassword

# API Keys
ALPHA_VANTAGE_KEY=your_api_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret

# Environment override
ENVIRONMENT=development
DEBUG_MODE=true
```

## Usage Examples

### 1. Basic Environment Switching

```bash
# Use development (default)
uv run --group chapter8 python environment_demo.py

# Use staging environment
ENVIRONMENT=staging uv run --group chapter8 python environment_demo.py

# Use production environment
ENVIRONMENT=production uv run --group chapter8 python environment_demo.py
```

### 2. Hydra with Environment Configs

```bash
# Default development environment
uv run --group chapter8 python hydra_environment_demo.py

# Override specific values
uv run --group chapter8 python hydra_environment_demo.py processing.batch_size=200

# Use different environment
uv run --group chapter8 python hydra_environment_demo.py --config-name=staging

# Multiple overrides
uv run --group chapter8 python hydra_environment_demo.py --config-name=production processing.debug_mode=true logging_level=DEBUG
```

### 3. Environment Variable Overrides

```bash
# Override debug mode via environment
DEBUG_MODE=false uv run --group chapter8 python environment_demo.py

# Override log level
LOG_LEVEL=WARNING uv run --group chapter8 python environment_demo.py

# Multiple environment overrides
ENVIRONMENT=staging DEBUG_MODE=true LOG_LEVEL=DEBUG uv run --group chapter8 python environment_demo.py
```

## Configuration Structure

Each environment config includes:

```yaml
# Data source configuration
data_source: csv|s3
file_path: path/to/data
bucket: s3-bucket-name  # for S3 sources

# Database settings
database:
  type: sqlite|postgresql
  host: hostname  # for PostgreSQL
  port: 5432
  user: username  # loaded from .env
  password: password  # loaded from .env

# Processing configuration
processing:
  batch_size: 100
  parallel_workers: 1
  cache_enabled: true
  debug_mode: false

# Model settings
model:
  save_path: path/to/model
  checkpoint_frequency: 10
  validation_split: 0.3

# API configuration
api:
  base_url: https://api.example.com
  timeout: 30
  retry_attempts: 3
```

## Security Best Practices

### ✅ What's Included in Config Files
- Non-sensitive settings (batch sizes, timeouts, paths)
- Environment-specific URLs and endpoints
- Feature configurations
- Processing parameters

### ❌ What's in .env Files Only
- Database passwords
- API keys and tokens
- Access credentials
- Sensitive URLs with tokens

### 🔒 Security Features
- `.env` files in `.gitignore`
- Environment variables override config values
- Secrets never logged or printed
- Production configs use strict security settings

## Advanced Features

### Config Value Interpolation
Environment configs support variable references:

```yaml
project:
  name: wine_quality
  version: v1

paths:
  base: data/${project.name}/${project.version}
  raw: ${paths.base}/raw
  processed: ${paths.base}/processed
```

### Conditional Logic
Different environments can have completely different structures:

```python
# Development uses local SQLite
if config['database']['type'] == 'sqlite':
    db_path = config['database']['path']

# Production uses PostgreSQL with SSL
elif config['database']['type'] == 'postgresql':
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{db}"
```

### Environment Detection
Automatic environment detection from various sources:

```python
environment = (
    os.getenv("ENVIRONMENT") or          # Explicit environment variable
    os.getenv("STAGE") or                # Alternative naming
    detect_from_hostname() or            # Auto-detect from hostname
    "development"                        # Safe default
)
```

## Troubleshooting

### Common Issues

1. **Config file not found**
   ```bash
   FileNotFoundError: Configuration file not found: config/staging.yaml
   ```
   - Ensure you're in the correct directory
   - Check that the config file exists
   - Verify the ENVIRONMENT variable value

2. **Missing environment variables**
   ```bash
   # Check if .env file exists and is loaded
   ls -la .env
   ```

3. **Hydra config errors**
   ```bash
   # Use --help to see available options
   uv run python hydra_environment_demo.py --help
   ```

### Debug Mode

Enable debug mode for detailed information:

```bash
DEBUG_MODE=true uv run --group chapter8 python environment_demo.py
```

## Integration with Other Tools

This example integrates with:
- **Hydra**: Advanced configuration management
- **python-dotenv**: Environment variable loading
- **PyYAML**: YAML file parsing
- **OmegaConf**: Configuration object handling

## Next Steps

After mastering environment configs:
1. Set up CI/CD pipelines with environment-specific deployments
2. Implement configuration validation with Pydantic
3. Add configuration versioning and migration tools
4. Integrate with secret management services (AWS Secrets Manager, etc.)