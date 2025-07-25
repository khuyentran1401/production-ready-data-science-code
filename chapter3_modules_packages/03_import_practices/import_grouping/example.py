# Standard library imports
import datetime
import os
import sys

# Third-party imports
import pandas as pd

# Local application imports
from utils import helpers


def demonstrate_proper_import_organization():
	"""Demonstrate how to properly organize imports following PEP 8 guidelines."""
	print("Import Organization Example")
	
	# Standard library usage
	current_time = datetime.datetime.now()
	python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
	current_dir = os.getcwd()
	
	# Third-party library usage  
	data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]}
	df = pd.DataFrame(data)
	
	# Local helper function usage
	helper_message = helpers()
	
	print(f"Current time: {current_time}")
	print(f"Python version: {python_version}")
	print(f"Directory: {current_dir}")
	print(f"DataFrame shape: {df.shape}")
	print(f"Helper says: {helper_message}")


if __name__ == "__main__":
	demonstrate_proper_import_organization()
