import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Création d'un jeu de données complet
dates = pd.date_range("2025-03-01", periods=60, freq="D")
df = pd.DataFrame({
    "temperature": np.random.normal(18, 3, size=60),
    "humidite": np.random.normal(55, 8, size=60),
    "vent": np.random.normal(15, 2, size=60)
}, index=dates)

# Fonction de traçage réutilisable
def plot_series(df, cols, titre):
    plt.figure(figsize=(9,4))
    for col in cols:
        plt.plot(df.index, df[col], marker=".", label=col)
    plt.title(titre)
    plt.xlabel("Date")
    plt.legend()
    plt.grid(True)
    plt.show()

# Tracé global
plot_series(df, ["temperature", "humidite", "vent"], "Évolution météo - mars 2025")

# Zoom + annotation
zoom = df.loc["2025-03-15":"2025-03-25"]
max_temp = zoom["temperature"].max()
max_date = zoom["temperature"].idxmax()

plt.plot(zoom.index, zoom["temperature"], color="red")
plt.title("Zoom sur la température (15-25 mars)")
plt.xlabel("Date")
plt.ylabel("Température (°C)")
plt.annotate(f"Pic {max_temp:.1f}°C", xy=(max_date, max_temp),
             xytext=(max_date, max_temp+0.5),
             arrowprops=dict(arrowstyle="->", color="black"))
plt.grid(True)
plt.show()
