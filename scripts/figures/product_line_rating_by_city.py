import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ProductSalesRatingByCity:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.canvas = None

    def draw_figure(self):
        df = pd.read_csv(self.file_path)

        # Calculate total rating by city and product line
        total_rating_by_city_product = df.groupby(['City', 'Product line'])['Rating'].sum().reset_index()

        # Create the grouped bar plot
        plt.figure(figsize=(12, 6))
        sns.barplot(x="Product line", y="Rating", hue="City", data=total_rating_by_city_product, palette="muted")
        plt.title("Total Product Rating by City and Product Line")
        plt.xlabel("Product Line")
        plt.ylabel("Total Rating")
        plt.legend(title="City", bbox_to_anchor=(1.05, 1), loc='best')
        plt.xticks(rotation=15)

        self.canvas = FigureCanvas(plt.gcf())
        if self.canvas:
            self.canvas.draw()
        else:
            self.canvas = FigureCanvas(plt.gcf())
            self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.canvas.updateGeometry()

        return self.canvas
