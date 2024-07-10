import pandas as pd
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class CityProductLineCorrelation:
    def __init__(self, table_widget: QTableWidget):
        self.table_widget = table_widget

    def load_data(self, file_path: str):
        interest_columns = ['City', 'Product line']
        df = pd.read_csv(file_path, usecols=interest_columns)

        df['City'] = df['City'].astype("category").cat.codes
        df['Product line'] = df['Product line'].astype("category").cat.codes

        correlation_matrix = df.corr()

        self.table_widget.setRowCount(len(correlation_matrix))
        self.table_widget.setColumnCount(len(correlation_matrix.columns))
        self.table_widget.setHorizontalHeaderLabels(correlation_matrix.columns)
        self.table_widget.setVerticalHeaderLabels(correlation_matrix.index)

        for i in range(len(correlation_matrix)):
            for j in range(len(correlation_matrix.columns)):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(round(correlation_matrix.iloc[i, j], 2))))