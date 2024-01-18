from scripts.run_project import DATA_PATH
from src.data_loader import DataLoader

# Load data
data_loader = DataLoader(DATA_PATH)
data = data_loader.load_data()

# add new column
data["countries"] = data.Hotel_Address.apply(lambda x: x.split(' ')[-1])

# show first 6 rows from countries column and unique values
print(data["countries"].unique())  # ['Netherlands' 'Kingdom' 'France' 'Spain' 'Italy' 'Austria']
