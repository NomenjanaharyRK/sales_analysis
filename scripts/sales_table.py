import pandas as pd
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class SalesTable:
    def __init__(self, table_widget: QTableWidget):
        self.table_widget = table_widget

    def load_data(self, file_path: str):
        interest_columns = ['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Total', 'Date', 'Time', 'Quantity', 'Rating']
        df = pd.read_csv(file_path, usecols=interest_columns)

        self.table_widget.setRowCount(len(df))
        self.table_widget.setColumnCount(len(df.columns))
        self.table_widget.setHorizontalHeaderLabels(df.columns)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))
