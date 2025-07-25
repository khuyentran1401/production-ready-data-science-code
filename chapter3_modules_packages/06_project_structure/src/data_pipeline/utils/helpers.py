"""Helper utility functions."""


def save_results(data: list, filename: str) -> None:
	"""Save processed data to a file.
	
	Args:
		data: List of processed data
		filename: Name of the output file
	"""
	with open(filename, "w") as f:
		f.write(str(data))
	print(f"Saved results to {filename}")
