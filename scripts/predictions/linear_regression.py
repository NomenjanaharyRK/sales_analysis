import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ProductSalesByCityLinearRegression:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.canvas = None

    def draw_figure(self):
        df = pd.read_csv(self.file_path)

        # Convertir les colonnes catégorielles en codes entiers
        categorical_columns = ['Branch', 'City', 'Customer type', 'Gender', 'Product line','Quantity', 'Unit price', 'Rating','Payment']
        for col in categorical_columns:
            df[col] = df[col].astype("category").cat.codes

        # Sélectionner les variables indépendantes et dépendantes
        X = df[['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Quantity', 'Unit price', 'Rating']]
        y = df['Total']

        # Diviser les données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Créer et entraîner le modèle de régression linéaire
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Faire des prédictions sur l'ensemble de test
        y_pred = model.predict(X_test)

        # Évaluer le modèle
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print("LinearRegression ====> Mean Squared Error:", mse)
        print("LinearRegression ====> R-squared:", r2)

        # Ajouter les prédictions aux données test
        X_test['Total'] = y_test
        X_test['Predicted Total'] = y_pred

        # Convertir les codes en catégories pour affichage
        product_line_mapping = pd.Categorical(df['Product line']).categories
        X_test['Product line'] = product_line_mapping[X_test['Product line'].values]

        # Visualiser les prédictions et les ventes actuelles
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Product line', y='Total', data=X_test, hue="Product line", palette='muted', errorbar=None)
        sns.lineplot(x='Product line', y='Predicted Total', data=X_test, color='red', alpha=0.7,
                     label='Predicted Total', errorbar=None)
        plt.xticks(rotation=15)
        plt.legend()
        plt.title('Actual vs Predicted Total Sales')

        self.canvas = FigureCanvas(plt.gcf())

        if self.canvas:
            self.canvas.draw()
        else:
            self.canvas = FigureCanvas(self.figure)
            self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.canvas.updateGeometry()

        return self.canvas