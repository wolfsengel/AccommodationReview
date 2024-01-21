from src.data_loader import DataLoader
from src.data_preprocessor import preprocess_data
from src.model import recommend_hotel

# Load data
data_loader = DataLoader()
data = data_loader.load_data()

# preprocess data
processed_data = preprocess_data(data)

# show first 5 rows
# print(processed_data.head())

# recommendation system

print(recommend_hotel(processed_data, "Netherlands", "Im going to Amsterdam for a week. Im going on a business trip."))
