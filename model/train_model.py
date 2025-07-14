# model/train_model.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Charger les données depuis un CSV public
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Garder les colonnes utiles et supprimer les lignes manquantes
df = df[["Pclass", "Sex", "Age", "Fare", "Survived"]].dropna()

# Encoder le sexe : male = 0, female = 1
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# Features et target
X = df[["Pclass", "Sex", "Age", "Fare"]]
y = df["Survived"]

# Split train/test (pas obligatoire ici, mais propre)
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle simple
model = LogisticRegression()
model.fit(X_train, y_train)

# Sauvegarder le modèle
joblib.dump(model, "model/model.pkl")
print("✅ Modèle entraîné et sauvegardé dans model.pkl")
