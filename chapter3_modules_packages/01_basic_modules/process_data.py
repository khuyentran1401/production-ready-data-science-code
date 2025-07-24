from pathlib import Path

import pandas as pd
from utils import config, save_to_csv

# Create sample data
X = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

# Use imported config
data_path = config["data_path"]
Path(data_path).mkdir(exist_ok=True)

# Use imported function
save_to_csv(f"{data_path}/mydata.csv", X)
