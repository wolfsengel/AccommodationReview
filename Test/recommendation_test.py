from scripts.run_project import DATA_PATH
from src.data_loader import DataLoader
from src.data_preprocessor import preprocess_data

# Load data
data_loader = DataLoader(DATA_PATH)
data = data_loader.load_data()

# preprocess data
processed_data = preprocess_data(data)

# show first 5 rows
# print(processed_data.head())
