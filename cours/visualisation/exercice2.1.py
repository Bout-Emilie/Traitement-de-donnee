import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
#  Lecture et préparation CSV
# -------------------------------
df = pd.read_csv("./meteo.csv")  # chemin vers le CSV
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")  # date comme index
print(df.head())

# -------------------------------
#  Fonction de traçage
# -------------------------------
def tracer_serie(df, colonne, titre, couleur, type_trace="line", annoter_max=False):
    plt.figure(figsize=(8,4))
    
    if type_trace == "line":
        plt.plot(df.index, df[colonne], color=couleur, marker="o")
    elif type_trace == "bar":
        plt.bar(df.index, df[colonne], color=couleur)
    elif type_trace == "scatter":
        plt.scatter(df.index, df[colonne], color=couleur)
    
    plt.title(titre)
    plt.xlabel("Date")
    plt.ylabel(colonne.capitalize())
    plt.grid(True)
    
    # annotation du maximum si demandé
    if annoter_max:
        max_val = df[colonne].max()
        max_date = df[colonne].idxmax()
        plt.annotate(f"Max: {max_val}", xy=(max_date, max_val),
                     xytext=(max_date, max_val + 1),
                     arrowprops=dict(facecolor='black', arrowstyle='->'))
    
    plt.show()

# -------------------------------
# Tracés individuels
# -------------------------------
tracer_serie(df, "temperature", "Température quotidienne", "tomato", "line", annoter_max=True)
tracer_serie(df, "pluie", "Précipitations journalières", "skyblue", "bar")
tracer_serie(df, "vent", "Vitesse du vent", "orange", "scatter")

# -------------------------------
#  Subplots pour comparer les 3 variables
# -------------------------------
fig, axes = plt.subplots(3, 1, figsize=(10,10))

# Température
axes[0].plot(df.index, df["temperature"], color="red", marker="o")
axes[0].set_title("Température quotidienne")
axes[0].set_ylabel("°C")
axes[0].grid(True)

# Pluie
axes[1].bar(df.index, df["pluie"], color="blue")
axes[1].set_title("Précipitations journalières")
axes[1].set_ylabel("mm")
axes[1].grid(True)

# Vent
axes[2].scatter(df.index, df["vent"], color="green")
axes[2].set_title("Vitesse du vent")
axes[2].set_ylabel("km/h")
axes[2].grid(True)

plt.tight_layout()
plt.show()

# -------------------------------
# Analyse hebdomadaire
# -------------------------------
# Moyenne hebdomadaire de la température
df_temp_weekly = df["temperature"].resample("W").mean()
tracer_serie(df_temp_weekly.to_frame(), "temperature", "Température moyenne hebdomadaire", "red", "line")

# Somme hebdomadaire des précipitations
df_rain_weekly = df["pluie"].resample("W").sum()
tracer_serie(df_rain_weekly.to_frame(), "pluie", "Précipitations hebdomadaires", "blue", "bar")

# -------------------------------
#  Combinaison pour comparaison
# -------------------------------
plt.figure(figsize=(10,5))
plt.bar(df_rain_weekly.index, df_rain_weekly, color="skyblue", label="Pluie cumulée")
plt.plot(df_temp_weekly.index, df_temp_weekly, color="red", marker="o", label="Température moyenne")
plt.title("Pluie et température hebdomadaire")
plt.xlabel("Date")
plt.ylabel("Valeurs")
plt.legend()
plt.grid(True)
plt.show()

