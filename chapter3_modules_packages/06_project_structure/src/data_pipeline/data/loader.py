"""Data loading functions."""


def load_data(filename: str) -> list:
	"""Load simple data for demonstration.
	
	Args:
		filename: Name of the file (ignored for simplicity)
		
	Returns:
		List of sample data
	"""
	data = [1, 2, 3, 4, 5, None, 7, 8, 9, 10]
	print(f"Loaded data from {filename}")
	return data
