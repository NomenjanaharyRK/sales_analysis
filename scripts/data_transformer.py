import pandas as pd

class DataTransformer:
    def __init__(self, data):
        self.data = data

    def transform_data_to_numeric(self):
        self.data = pd.get_dummies(self.data, drop_first= True)
        return self.data
