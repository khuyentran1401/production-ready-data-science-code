"""
Basic Hydra configuration example from Chapter 8.

This demonstrates the exact example shown in the book.
"""

import hydra
from omegaconf import DictConfig


@hydra.main(
    config_path="config", config_name="main", version_base=None
)
def process_data(config: DictConfig):
    # You can use a bracket notation
    print(config["process"]["cols_to_drop"])
    
    # Or dot notation
    print(config.process.feature)
    print(config.process.test_size)


if __name__ == "__main__":
    process_data()