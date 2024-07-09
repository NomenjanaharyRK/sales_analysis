import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class SalesAnalysisApp(QWidget):
    def __init__(self):
        super().__init__()

        self.data = None

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.load_button = QPushButton('Load Data', self)
        self.load_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_button)

        self.transform_button = QPushButton('Transform Data', self)
        self.transform_button.clicked.connect(self.transform_data)
        layout.addWidget(self.transform_button)

        self.correlation_button = QPushButton('Calculate Correlation', self)
        self.correlation_button.clicked.connect(self.calculate_correlation)
        layout.addWidget(self.correlation_button)

        self.plot_button = QPushButton('Plot Graph', self)
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        self.data_label = QLabel('No data loaded', self)
        layout.addWidget(self.data_label)

        self.table = QTableView(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.setWindowTitle('Sales Data Analysis')
        self.show()

    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open CSV File', './', 'CSV files (*.csv)')
        if file_path:
            loader = DataLoader(file_path)
            self.data = loader.load_data()
            if self.data is not None:
                self.update_table(self.data)

    def transform_data(self):
        if self.data is not None:
            transformer = DataTransformer(self.data)
            self.data = transformer.transform_to_numeric()
            self.update_table(self.data)

    def calculate_correlation(self):
        if self.data is not None:
            analyzer = CorrelationAnalyzer(self.data)
            correlation_matrix = analyzer.calculate_correlation()
            print(correlation_matrix)

    def plot_graph(self):
        if self.data is not None:
            sns.pairplot(self.data)
            plt.show()

    def update_table(self, data):
        model = QStandardItemModel(data.shape[0], data.shape[1])
        model.setHorizontalHeaderLabels(data.columns)

        for row in range(data.shape[0]):
            for column in range(data.shape[1]):
                item = QStandardItem(str(data.iloc[row, column]))
                model.setItem(row, column, item)

        self.table.setModel(model)
        self.data_label.setText('Data loaded successfully')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SalesAnalysisApp()
    sys.exit(app.exec_())
