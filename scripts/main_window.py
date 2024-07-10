import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QStackedWidget, QTableWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from sales_table import SalesTable
from sales_numerics_table import SalesNumericsTable
from city_product_line_correlation_table import CityProductLineCorrelation
from gender_product_line_table import GenderProductLineCorrelation
from city_gender_correlation_table import CityGenderCorrelation
from city_customer_type_correlation_table import CityCustomerTypeCorrelation
from product_line_client_type import ProductLineCustomerTypeCorrelation


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../sales_analysis.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.product_line_client_type_canvas = None

        self.exit_app_btn = self.findChild(QPushButton, "exit_app_btn")
        self.exit_app_btn.clicked.connect(self.close)

        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        self.stackedWidget.setCurrentIndex(7)

        self.sales_table_widget = self.findChild(QTableWidget, "sales_table")
        self.sales_table = SalesTable(self.sales_table_widget)

        self.sales_numeric_table = self.findChild(QTableWidget, "sales_numeric_table")
        self.sales_numeric_table = SalesNumericsTable(self.sales_numeric_table)

        self.gender_product_line_table = self.findChild(QTableWidget, "gender_product_line_table")
        self.gender_product_line_table = GenderProductLineCorrelation(self.gender_product_line_table)

        self.city_product_line_correlation_table = self.findChild(QTableWidget, "city_product_line_correlation_table")
        self.city_product_line_correlation_table = CityProductLineCorrelation(self.city_product_line_correlation_table)

        self.city_gender_correlation_table = self.findChild(QTableWidget, "city_gender_correlation_table")
        self.city_gender_correlation_table = CityGenderCorrelation(self.city_gender_correlation_table)

        self.city_client_type_table = self.findChild(QTableWidget, "city_client_type_table")
        self.city_client_type_table = CityCustomerTypeCorrelation(self.city_client_type_table)

        self.product_line_client_type_table = self.findChild(QTableWidget, "product_line_client_type_table")
        self.product_line_client_type_table = ProductLineCustomerTypeCorrelation(self.product_line_client_type_table)

        # Widget for figure
        self.correlation_figure_product_line_client_type = self.findChild(QWidget, "correlation_figure_product_line_client_type")
        self.product_line_customer_type_layout = self.findChild(QVBoxLayout, "product_line_customer_type_layout")

        # SETTINGS SIDEBAR BUTTONS
        self.sales_table_btn = self.findChild(QPushButton, "sales_table_btn")
        self.sale_numeric_table_btn = self.findChild(QPushButton, "sale_numeric_table_btn")
        self.product_line_city_btn = self.findChild(QPushButton, "product_line_city_btn")
        self.product_line_gender_btn = self.findChild(QPushButton, "product_line_gender_btn")
        self.city_gender_btn = self.findChild(QPushButton, "city_gender_btn")
        self.city_client_type_btn = self.findChild(QPushButton, "city_client_type_btn")
        self.product_line_client_type_btn = self.findChild(QPushButton, "product_line_client_type_btn")

        # CONNECT BUTTONS FUNCTION
        self.sales_table_btn.clicked.connect(self.show_sales_table_page)
        self.sale_numeric_table_btn.clicked.connect(self.show_sales_numeric_table_page)
        self.product_line_city_btn.clicked.connect(self.show_product_line_city_page)
        self.product_line_gender_btn.clicked.connect(self.show_product_line_gender_page)
        self.city_gender_btn.clicked.connect(self.show_city_gender_page)
        self.city_client_type_btn.clicked.connect(self.show_city_client_type_page)
        self.product_line_client_type_btn.clicked.connect(self.show_product_line_client_type_page)

        # Load data into the pages
        self.sales_table.load_data('../data/supermarket_sales_data.csv')
        self.sales_numeric_table.load_data('../data/supermarket_sales_data.csv')
        self.city_product_line_correlation_table.load_data('../data/supermarket_sales_data.csv')
        self.gender_product_line_table.load_data('../data/supermarket_sales_data.csv')
        self.city_gender_correlation_table.load_data('../data/supermarket_sales_data.csv')
        self.city_client_type_table.load_data('../data/supermarket_sales_data.csv')
        self.product_line_client_type_table.load_data('../data/supermarket_sales_data.csv')

        self.add_correlation_plot()

    def add_correlation_plot(self):
        self.product_line_client_type_canvas = self.product_line_client_type_table.draw_figure()
        self.product_line_customer_type_layout.addWidget(self.product_line_client_type_canvas)

    def show_sales_table_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_sales_numeric_table_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_product_line_city_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_product_line_gender_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_city_gender_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def show_city_client_type_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def show_product_line_client_type_page(self):
        self.stackedWidget.setCurrentIndex(6)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
