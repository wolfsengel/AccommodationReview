from src.data_loader import DataLoader
from src.evaluation import get_recommendations

# Load data
data_loader = DataLoader()
data = data_loader.load_data()

# recommend hotels
print(get_recommendations(60,))