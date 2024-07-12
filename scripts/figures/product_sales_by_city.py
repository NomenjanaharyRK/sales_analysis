import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ProductSalesByCity:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.canvas = None

    def draw_figure(self):
        df = pd.read_csv(self.file_path)

        # Create the grouped bar plot
        plt.figure(figsize=(12, 6))
        sns.barplot(x="Product line", y="Total", hue="City", data=df, errorbar=None)
        plt.title("Product line sales by City")
        plt.xlabel("Product line")
        plt.ylabel("Total Sales")
        plt.legend(title="City", loc='upper right')

        self.canvas = FigureCanvas(plt.gcf())

        if self.canvas:
            self.canvas.draw()
        else:
            self.canvas = FigureCanvas(self.figure)
            self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.canvas.updateGeometry()

        return self.canvas
