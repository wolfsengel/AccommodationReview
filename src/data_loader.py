import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        if file_path is None:
            raise Exception("File path cannot be None")
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path)
        return data
