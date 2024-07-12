import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class CorrelationSalesFigure:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.figure = None
        self.canvas = None

    def draw_figure(self):
        interest_columns = ['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Total', 'Date', 'Time', 'Quantity', 'Rating']
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

        correlation_matrix = df.corr()

        if self.figure:
            self.figure.clear()

        self.figure, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)

        if self.canvas:
            self.canvas.draw()
        else:
            self.canvas = FigureCanvas(self.figure)
            self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.canvas.updateGeometry()

        return self.canvas
