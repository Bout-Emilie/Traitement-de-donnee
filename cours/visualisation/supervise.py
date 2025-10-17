import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("./meteo_365.csv")
print(df.head())

# lE BUT predire la temperature en fonction des donnees hunidite - pression - vent 
X = df[["humidite", "pression", "vent"]]  # variables explicatives
y = df["temperature"]                   

#On divise le jeu de donnees: 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -------------------------------
# 3️Création et entraînement du modèle
# -------------------------------
model = LinearRegression() # On a choisi le model LinearRegression 
model.fit(X_train, y_train) #On entraine le model

# -------------------------------
# Prédiction sur le jeu de test
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# Évaluation de notre model
# -------------------------------
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE : {mse:.2f}")
print(f"R² : {r2:.2f}")

# -------------------------------
# Visualisation prédictions vs réelles
# -------------------------------
plt.figure()
plt.plot(y_test.index, y_test, label="Réel", marker="o")
plt.plot(y_test.index, y_pred, label="Prédit", marker="x")
plt.title("Prédiction supervisée de la température")
plt.xlabel("Index des données")
plt.ylabel("Température (°C)")
plt.legend()
plt.grid(True)
plt.show()


# -------------------------------
# 7️⃣ Exemple prédiction nouvelle journée
# -------------------------------
nouveau_jour = pd.DataFrame({
    "humidite": [84],
    "pression": [1010],
    "vent": [12]
})
prediction = model.predict(nouveau_jour)
print(f"Température prédite pour le nouveau jour : {prediction[0]:.1f} °C")