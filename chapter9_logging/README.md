# Chapter 9: Logging Examples

This directory contains examples for logging with Loguru as demonstrated in Chapter 9 of the book.

## Examples Overview

### 1. Basic Logging (`01_basic_logging/`)
- Introduction to Loguru's out-of-the-box functionality
- Different log levels (debug, info, warning, error)
- Colorful and informative logs by default

### 2. Custom Formatting (`02_custom_formatting/`)
- Customizing log output format
- Using `logger.remove()` and `logger.add()`
- Time formatting and metadata inclusion

### 3. File Logging (`03_file_logging/`)
- Logging to both terminal and file simultaneously
- File handlers with custom formats
- Level-based filtering

### 4. Rotation and Retention (`04_rotation_retention/`)
- Log file rotation strategies (size, time, periodic)
- Retention policies for old logs
- Log compression options

### 5. Filtering (`05_filtering/`)
- Message filtering using lambda functions
- Selective logging based on content
- Simple filtering without complex classes

### 6. Exception Handling (`06_exception_handling/`)
- Enhanced exception logging with full tracebacks
- `@logger.catch` decorator for automatic exception catching
- Detailed debugging information

### 7. Colorized Logs (`07_colorized_logs/`)
- Custom color schemes for log output
- Color tags and level-based coloring
- Enhanced readability

## Prerequisites

Install dependencies using:
```bash
uv sync --group chapter9
```

## Key Concepts Covered

1. **Why Loguru?**:
   - Combines power of logging with simplicity of print statements
   - Elegant out-of-the-box functionality
   - Colorful and informative logs by default

2. **Loguru Features**:
   - Simple configuration with `logger.add()`
   - Flexible formatting with tokens (`{time}`, `{level}`, `{message}`)
   - Easy file logging and rotation
   - Lambda-based filtering
   - Enhanced exception handling
   - Colorized output

3. **Best Practices**:
   - Use appropriate log levels
   - Include relevant metadata (module, function, line)
   - Implement log rotation for production systems
   - Filter logs appropriately for different outputs
   - Use exception logging for better debugging

## Running All Examples

Each subdirectory contains its own README with specific instructions. Generally:

```bash
# Navigate to any example directory
cd 01_basic_logging/

# Run the example
uv run --group chapter9 python <script_name>.py
```

## Log Output Files

Some examples generate log files:
- `info.log` - Basic file logging output
- `hello.log` - Filtered logs containing "Hello"
- `debug.log` - Rotated logs with retention
- `logs/` directory - Various rotation strategies

These files are created in the respective example directories when you run the scripts.