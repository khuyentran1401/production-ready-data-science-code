"""
Hydra interpolation example from Chapter 8.

This demonstrates how to use interpolation to reduce config duplication.
"""

import hydra
from omegaconf import DictConfig


@hydra.main(
    config_path="config", config_name="main", version_base=None
)
def show_interpolation(config: DictConfig):
    print("Project info:")
    print(f"  Name: {config.project.name}")
    print(f"  Version: {config.project.version}")
    
    print("\nPaths (using interpolation):")
    print(f"  Base: {config.paths.base}")
    print(f"  Raw: {config.paths.raw}")
    print(f"  Processed: {config.paths.processed}")
    print(f"  Reports: {config.paths.reports}")


if __name__ == "__main__":
    show_interpolation()