import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class SalesStatisticsTable:
    def __init__(self, table_widget: QTableWidget, file_path: str):
        self.table_widget = table_widget
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        df = pd.read_csv(self.file_path)

        statistics = df.describe()

        self.table_widget.setRowCount(len(statistics))
        self.table_widget.setColumnCount(len(statistics.columns))
        self.table_widget.setHorizontalHeaderLabels(statistics.columns)
        self.table_widget.setVerticalHeaderLabels(statistics.index)

        for i in range(len(statistics)):
            for j in range(len(statistics.columns)):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(statistics.iloc[i, j])))
