import pandas as pd
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class SalesStatisticsTable:
    def __init__(self, table_widget: QTableWidget, file_path: str):
        self.table_widget = table_widget
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        interest_columns = ['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Total', 'Date','Time', 'Quantity', 'Rating']
        df = pd.read_csv(self.file_path, usecols=interest_columns)

        df['Invoice ID'] = df['Invoice ID'].astype("category").cat.codes
        df['Branch'] = df['Branch'].astype("category").cat.codes
        df['City'] = df['City'].astype("category").cat.codes
        df['Customer type'] = df['Customer type'].astype("category").cat.codes
        df['Gender'] = df['Gender'].astype("category").cat.codes
        df['Product line'] = df['Product line'].astype("category").cat.codes
        df['Total'] = df['Total'].astype("category").cat.codes
        df['Date'] = df['Date'].astype("category").cat.codes
        df['Time'] = df['Time'].astype("category").cat.codes
        df['Quantity'] = df['Quantity'].astype("category").cat.codes
        df['Rating'] = df['Rating'].astype("category").cat.codes

        statistics = df.describe()

        self.table_widget.setRowCount(len(statistics))
        self.table_widget.setColumnCount(len(statistics.columns))
        self.table_widget.setHorizontalHeaderLabels(statistics.columns)
        self.table_widget.setVerticalHeaderLabels(statistics.index)

        for i in range(len(statistics)):
            for j in range(len(statistics.columns)):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(statistics.iloc[i, j])))

