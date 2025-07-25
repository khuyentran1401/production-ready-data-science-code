"""
Hydra config groups example from Chapter 8.

This demonstrates how to organize configurations into logical groups.
"""

import hydra
from omegaconf import DictConfig


@hydra.main(
    config_path="config", config_name="main", version_base=None
)
def process_with_groups(config: DictConfig):
    print("Data paths:")
    print(f"  Raw: {config.data.raw}")
    print(f"  Intermediate: {config.data.intermediate}")
    
    print(f"\nProcessing strategy: {config.strategy}")
    
    if config.strategy == "drop_missing":
        print("Columns to drop:")
        for col in config.cols_to_drop:
            print(f"  - {col}")
    
    elif config.strategy == "impute":
        print(f"Impute method: {config.impute_method}")
        print("Columns to impute:")
        for col in config.cols_to_impute:
            print(f"  - {col}")
    
    print(f"\nTarget feature: {config.feature}")
    print(f"Test size: {config.test_size}")


if __name__ == "__main__":
    process_with_groups()