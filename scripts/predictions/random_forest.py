import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ProductSalesByCityRandomForest:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.canvas = None

    def draw_figure(self):
        df = pd.read_csv(self.file_path)

        # Encoder la colonne "Product line" en utilisant l'encodage one-hot
        df_encoded = pd.get_dummies(df, columns=["Product line"])

        # Selectionner les variables dependantes et independantes
        X = df_encoded[['Product line_Electronic accessories', 'Product line_Fashion accessories',
                        'Product line_Food and beverages', 'Product line_Health and beauty',
                        'Product line_Home and lifestyle', 'Product line_Sports and travel']]
        y = df_encoded['Total']

        # Diviser les données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Créer et entraîner le modèle de forêt aléatoire
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Faire des prédictions sur l'ensemble de test
        y_pred = model.predict(X_test)

        # Évaluer le modèle
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print("randomForest ====> Mean Squared Error:", mse)
        print("randomForest ====> R-squared:", r2)

        # Ajouter les prédictions aux données test
        X_test['Total'] = y_test
        X_test['Predicted Total'] = y_pred

        # Ajouter la colonne 'Product line' originale pour visualisation
        X_test = X_test.merge(df[['Product line']], left_index=True, right_index=True)

        # Visualiser les prédictions et les ventes actuelles
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Product line', y='Total', data=X_test, hue="Product line", palette='muted', errorbar=None)
        sns.lineplot(x='Product line', y='Predicted Total', data=X_test, color='red', alpha=0.7, label='Predicted Total', errorbar=None)
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
