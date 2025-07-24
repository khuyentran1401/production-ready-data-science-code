"""Main pipeline execution script demonstrating project structure."""

from data_pipeline.data import load_data, process_data 
from data_pipeline.utils import save_results


def main():
	"""Execute a simple data pipeline to demonstrate project structure."""
	print("Starting Data Pipeline")
	
	# 1. Load data
	print("Loading data...")
	data = load_data("sample_data.csv")
	
	# 2. Process data
	print("Processing data...")
	processed_data = process_data(data)
	
	# 3. Save results
	print("Saving results...")
	save_results(processed_data, "output.txt")
	
	print("Pipeline completed!")


if __name__ == "__main__":
	main()
