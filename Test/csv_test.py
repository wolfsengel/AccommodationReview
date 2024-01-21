from src.data_loader import DataLoader

# Load data
data_loader = DataLoader()
data = data_loader.load_data()
# show first 5 rows
print(data.head())

# show specific column and first 5 rows
print(data["Hotel_Address"].head())
