import pandas as pd
import os

DATA_PATH = os.path.join('..', 'data', 'Accommodation_Reviews.csv')


class DataLoader:
    def __init__(self):
        if DATA_PATH is None:
            raise Exception("File path cannot be None")
        self.file_path = DATA_PATH

    def load_data(self):

        # Load the dataset
        data = pd.read_csv(self.file_path)

        # Data Sample of 10% of the dataset to reduce computational cost
        # data = data.sample(frac=0.5, replace=False, random_state=42)
        return data
