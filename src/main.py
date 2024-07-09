import sys

import pandas as pd
from PyQt5.QtWidgets import QApplication
from data_analysis import SalesDataAnalysis
from dashboard import Dashboard

def main():
    app = QApplication(sys.argv)

    # Load Data
    df = pd.read_csv("../data/supermarket_sales_sheet1.csv")

    df["City"] = df["City"].astype('category').cat.codes
    df["Gender"] = df["Gender"].astype('category').cat.codes
    df["Customer type"] = df["Customer type"].astype('category').cat.codes
    df["Product line"] = df["Product line"].astype('category').cat.codes
    df["Branch"] = df["Branch"].astype('category').cat.codes

    # Create Analysis Object
    analysis = SalesDataAnalysis(df)

    # Create and show Dashboard
    dashboard = Dashboard(analysis)
    dashboard.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()