"""Data processing functions."""


def process_data(data: list) -> list:
	"""Process data by removing None values and multiplying by 2.
	
	Args:
		data: List of data to process
		
	Returns:
		Processed data list
	"""
	# Remove None values
	cleaned = [x for x in data if x is not None]
	
	# Transform data
	processed = [x * 2 for x in cleaned]
	
	print(f"Processed {len(processed)} data points")
	return processed
