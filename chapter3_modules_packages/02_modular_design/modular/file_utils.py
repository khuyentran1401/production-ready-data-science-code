def save_results(data):
	"""Save results to a file."""
	with open("results.txt", "w") as f:
		f.write(str(data))
	print("Results saved")