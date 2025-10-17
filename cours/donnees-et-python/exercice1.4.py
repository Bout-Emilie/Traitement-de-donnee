import pandas as pd

# 1️⃣ Étape 1 : Lecture du fichier Parquet
# Lecture uniquement des colonnes nécessaires pour économiser la mémoire

colonnes_utiles = ["Produit", "Quantite", "Prix", "Ville"]

df = pd.read_parquet("data.parquet", columns=colonnes_utiles)

print(df.head())

# Étape 2 : Optimisation des types de données

df["Quantite"] = df["Quantite"].astype("int32")

df["Prix"] = df["Prix"].astype("float32")

#  Étape 3 : Calcul du montant de chaque vente

df["montant_total"] = df["Quantite"] * df["Prix"]

#  Étape 4 : Agrégation par ville
ca_par_ville = df.groupby("Ville")["montant_total"].sum().reset_index()

print(ca_par_ville)

#  Étape 5 : Sauvegarde du résultat optimisée en Parquet compressé
ca_par_ville.to_parquet("ca_par_ville.parquet", compression="snappy")