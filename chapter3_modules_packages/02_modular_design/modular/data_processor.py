def clean_data(data):
	"""Clean the data by removing None values."""
	cleaned = [x for x in data if x is not None]
	print("Data cleaned")
	return cleaned


def transform_data(data):
	"""Transform data by multiplying each value by 2."""
	transformed = [x * 2 for x in data]
	print("Data transformed")
	return transformed