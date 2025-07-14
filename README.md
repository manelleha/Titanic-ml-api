# 🚢 Titanic Survival Prediction API

Ce projet expose une API de prédiction de survie à bord du Titanic, entraînée sur le dataset Titanic de Kaggle.  
L’objectif est de déployer un modèle de Machine Learning via une API REST en utilisant FastAPI et Docker.

---

## 📁 Structure du projet

```
titanic_ml_api/
├── app/
│   └── main.py               # API FastAPI
├── model/
│   ├── train_model.py        # Script d'entraînement
│   └── model.pkl             # Modèle entraîné (généré)
├── tests/
│   └── test_main.py          # Test unitaire de l'API
├── Dockerfile                # Image Docker pour l'API
├── docker-compose.yml        # Lancement via Docker Compose
├── requirements.txt          # Dépendances Python
└── README.md                 # Ce fichier
```

---

## ⚙️ 1. Installer les dépendances (en local)

Si tu veux exécuter l’API sans Docker :

```bash
pip install -r requirements.txt
```

Puis entraîne et sauvegarde le modèle :

```bash
python model/train_model.py
```

Lance ensuite l'API :

```bash
uvicorn app.main:app --reload
```

Ouvre ton navigateur à l’adresse :  
➡️ `http://127.0.0.1:8000`

La documentation Swagger est accessible ici :  
➡️ `http://127.0.0.1:8000/docs`

---

## 🐳 2. Lancer via Docker

### Étapes :

1. Construire l’image Docker :
   ```bash
   docker build -t titanic-api -f Dockerfile .
   ```

2. Lancer le conteneur :
   ```bash
   docker run -p 8000:8000 titanic-api
   ```

> Ouvre ton navigateur sur `http://localhost:8000/docs` pour utiliser l'API.

---

## 🐳✅ 3. Lancer avec Docker Compose (plus simple)

```bash
docker-compose up --build
```

Accès API :
- Swagger UI : `http://localhost:8000/docs`
- Racine : `http://localhost:8000`

---

## 🧪 4. Lancer les tests

Assure-toi d'avoir installé les dépendances :

```bash
pip install -r requirements.txt
```

Puis lance les tests avec :

```bash
pytest tests/test_main.py
```

---

## 📤 Requête POST attendue

Endpoint : `/predict`  
Méthode : POST  
Exemple de corps JSON :

```json
{
  "Pclass": 3,
  "Sex": 1,
  "Age": 22.0,
  "Fare": 7.25
}
```

Réponse attendue :

```json
{
  "prediction": 0
}
```

---

## ✅ Technologies utilisées

- Python 3.10
- FastAPI
- Scikit-learn
- Docker & Docker Compose
- Pytest

---

