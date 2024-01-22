from src.data_loader import DataLoader
# Load data
data_loader = DataLoader()
data = data_loader.load_data()

# show hotel_names unique number
print(len(data["Hotel_Name"].unique()))  # 1492
