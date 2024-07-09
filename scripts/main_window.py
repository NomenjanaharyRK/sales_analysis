import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../sales_analysis.ui", self)

        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")

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
