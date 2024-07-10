import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ProductLineCustomerTypeCorrelation:
    def __init__(self, table_widget: QTableWidget):
        self.table_widget = table_widget
        self.correlation_matrix = None
        self.figure = None
        self.canvas = None

    def load_data(self, file_path: str):
        interest_columns = ['Product line', 'Customer type']
        df = pd.read_csv(file_path, usecols=interest_columns)

        df['Product line'] = df['Product line'].astype("category").cat.codes
        df['Customer type'] = df['Customer type'].astype("category").cat.codes

        correlation_matrix = df.corr()

        self.table_widget.setRowCount(len(correlation_matrix))
        self.table_widget.setColumnCount(len(correlation_matrix.columns))
        self.table_widget.setHorizontalHeaderLabels(correlation_matrix.columns)
        self.table_widget.setVerticalHeaderLabels(correlation_matrix.index)

        for i in range(len(correlation_matrix)):
            for j in range(len(correlation_matrix.columns)):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(round(correlation_matrix.iloc[i, j], 2))))

        self.correlation_matrix = correlation_matrix

    def draw_figure(self):
        if self.figure:
            self.figure.clear()

        self.figure, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(self.correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)

        if self.canvas:
            self.canvas.draw()
        else:
            self.canvas = FigureCanvas(self.figure)
            self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.canvas.updateGeometry()

        return self.canvas
