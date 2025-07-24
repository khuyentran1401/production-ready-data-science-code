"""Utility functions for the import grouping example."""


def helpers():
    """Placeholder helper function to demonstrate local imports."""
    return "Local helper function imported successfully!"


def format_results(results_dict):
    """Format results dictionary for display."""
    formatted = []
    for key, value in results_dict.items():
        formatted.append(f"{key}: {value}")
    return "\n".join(formatted)
