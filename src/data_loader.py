import pandas as pd
import os

DATA_PATH = os.path.join('..', 'data', 'Accommodation_Reviews.csv')


class DataLoader:
    def __init__(self):
        if DATA_PATH is None:
            raise Exception("File path cannot be None")
        self.file_path = DATA_PATH

    def load_data(self):
        data = pd.read_csv(self.file_path)
        return data
