import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi= dpi)
        super(MplCanvas, self).__init__(fig)

class Dashboard(QMainWindow):
    def __init__(self, analysis):
        super().__init__()
        self.analysis = analysis
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sales Data Analysis Dashboard")

        layout = QVBoxLayout()

        self.canvas = MplCanvas(self, width=10, height=6)
        layout.addWidget(self.canvas)

        btn_city_product_line = QPushButton("Show City and Product Line Correlation ")
        btn_city_product_line.clicked.connect(self.plot_city_product_line)
        layout.addWidget(btn_city_product_line)

        btn_city_gender = QPushButton("Show City and Render Correlation")
        btn_city_gender.clicked.connect(self.plot_city_gender)
        layout.addWidget(btn_city_gender)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def plot_city_product_line(self):
        self.canvas.ax.clear()
        self.analysis.correlation_city_product_line(ax=self.canvas.ax)
        self.canvas.draw()

    def plot_city_gender(self):
        self.canvas.ax.clear()
        self.analysis.correlation_city_gender(ax=self.canvas.ax)
        self.canvas.draw()