import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class SalesDataAnalysis:
    def __init__(self, dataframe):
        self.df = dataframe

    def correlation_city_product_line(self, ax):
        sns.countplot(x='City', hue='Product line', data= self.df, ax=ax)
        ax.set_title('Correlation between City and Product line')

    def correlation_city_gender(self, ax):
        sns.countplot(x='City', hue='Gender', data=self.df, ax=ax)
        ax.set_title('Correlation between City and Gender')