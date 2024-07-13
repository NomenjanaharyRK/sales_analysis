import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ProductSalesByCityAndGender:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.canvas = None

    def draw_figure(self):
        df = pd.read_csv(self.file_path)

        # Get the order of the product lines
        product_order = df["Product line"].unique()

        # Create a FacetGrid bar plot
        g = sns.FacetGrid(df, col="City", row="Gender", margin_titles=True, height=1.5, aspect=2.8)
        g.map_dataframe(sns.barplot, x="Product line", y="Total", hue=df["Product line"], errorbar=None, palette="muted", order=product_order)
        g.set_axis_labels("Product Type", "Total Sales")
        g.set_titles(col_template="{col_name}", row_template="{row_name}")

        for ax in g.axes.flat:
            for label in ax.get_xticklabels():
                label.set_rotation(90)

        self.canvas = FigureCanvas(plt.gcf())
        if self.canvas:
            self.canvas.draw()
        else:
            self.canvas = FigureCanvas(plt.gcf())
            self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.canvas.updateGeometry()

        return self.canvas
