import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QStackedWidget, QTableWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from scripts.tables.sales_table import SalesTable
from scripts.tables.sales_numerics_table import SalesNumericsTable
from scripts.tables.sales_statistics_table import SalesStatisticsTable
from scripts.figures.correlation_sales_figure import CorrelationSalesFigure
from scripts.figures.product_sales_by_city import ProductSalesByCity
from scripts.figures.product_line_by_city_and_gender import ProductSalesByCityAndGender


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../sales_analysis.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        self.stackedWidget.setCurrentIndex(7)

        self.sales_data_csv = "../data/supermarket_sales_data.csv"

        # TableWidget Setting
        self.sales_table_widget = self.findChild(QTableWidget, "sales_table")
        self.sales_numeric_table = self.findChild(QTableWidget, "sales_numeric_table")
        self.sales_statistics_table = self.findChild(QTableWidget, "sales_statistics_table")

        self.sales_table = SalesTable(self.sales_table_widget, self.sales_data_csv)
        self.sales_numeric_table = SalesNumericsTable(self.sales_numeric_table, self.sales_data_csv)
        self.sales_statistics_table = SalesStatisticsTable(self.sales_statistics_table, self.sales_data_csv)

        # Figures Widgets
        self.correlation_sales_widget = self.findChild(QWidget, "correlation_sales_widget")
        self.correlation_sales_layout = self.findChild(QVBoxLayout, "correlation_sales_layout")

        self.relation_product_line_gender_city_widget = self.findChild(QWidget, "relation_product_line_gender_city")
        self.relation_product_line_city_layout = self.findChild(QVBoxLayout, "relation_product_line_gender_city_layout")

        self.product_line_city_gender_widget = self.findChild(QWidget, "product_line_city_gender_widget")
        self.relation_product_line_city_gender_layout = self.findChild(QVBoxLayout, "product_line_city_gender_layout")

        # Draw Figures
        self.correlation_sales_figure = CorrelationSalesFigure(self.sales_data_csv)
        self.sales_correlation_canvas = self.correlation_sales_figure.draw_figure()
        self.correlation_sales_layout.addWidget(self.sales_correlation_canvas)

        self.product_sales_by_city = ProductSalesByCity(self.sales_data_csv)
        self.relation_product_line_by_city_canvas = self.product_sales_by_city.draw_figure()
        self.relation_product_line_city_layout.addWidget(self.relation_product_line_by_city_canvas)

        self.product_sales_by_city_gender = ProductSalesByCityAndGender(self.sales_data_csv)
        self.relation_product_line_by_city_gender_canvas = self.product_sales_by_city_gender.draw_figure()
        self.relation_product_line_city_gender_layout.addWidget(self.relation_product_line_by_city_gender_canvas)

        # SideBar Buttons Setting
        self.sales_table_btn = self.findChild(QPushButton, "sales_table_btn")
        self.sales_numeric_table_btn = self.findChild(QPushButton, "sales_numeric_table_btn")
        self.sales_statistics_table_btn = self.findChild(QPushButton, "sales_statistics_table_btn")
        self.correlation_sales_btn = self.findChild(QPushButton, "correlation_sales_btn")
        self.product_line_sales_by_city_btn = self.findChild(QPushButton, "product_line_sales_by_city_btn")
        self.product_line_sales_by_city_gender_btn = self.findChild(QPushButton, "product_line_sales_by_city_gender_btn")
        self.correlation_product_line_rating_btn = self.findChild(QPushButton, "correlation_product_line_rating_btn")
        self.correlation_product_line_city_branch_btn = self.findChild(QPushButton, "correlation_product_line_city_branch_btn")
        self.correlation_product_line_city_client_type = self.findChild(QPushButton, "correlation_product_line_city_client_type")
        self.product_line_client_type_btn = self.findChild(QPushButton, "product_line_client_type_btn")
        self.exit_app_btn = self.findChild(QPushButton, "exit_app_btn")

        # Connect SideBar Buttons
        self.exit_app_btn.clicked.connect(self.close)
        self.sales_table_btn.clicked.connect(self.show_sales_table)
        self.sales_numeric_table_btn.clicked.connect(self.show_sales_numeric_table)
        self.sales_statistics_table_btn.clicked.connect(self.show_sales_statistics_table)
        self.correlation_sales_btn.clicked.connect(self.show_correlation_sales)
        self.product_line_sales_by_city_btn.clicked.connect(self.show_product_line_sales_by_city)
        self.product_line_sales_by_city_gender_btn.clicked.connect(self.show_product_line_sales_by_city_and_genre)
        self.correlation_product_line_rating_btn.clicked.connect(self.show_correlation_product_line_rating)
        self.correlation_product_line_city_branch_btn.clicked.connect(self.show_correlation_product_line_city_branch)
        self.correlation_product_line_city_client_type.clicked.connect(self.show_correlation_product_line_city_client_type)

    def show_sales_table(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_sales_numeric_table(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_sales_statistics_table(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_correlation_sales(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_product_line_sales_by_city(self):
        self.stackedWidget.setCurrentIndex(4)

    def show_product_line_sales_by_city_and_genre(self):
        self.stackedWidget.setCurrentIndex(5)

    def show_correlation_product_line_rating(self):
        self.stackedWidget.setCurrentIndex(6)

    def show_correlation_product_line_city_branch(self):
        self.stackedWidget.setCurrentIndex(8)

    def show_correlation_product_line_city_client_type(self):
        self.stackedWidget.setCurrentIndex(9)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
