# 📊 Carte de Criticité des Logements en France

Ce projet permet d'analyser et de visualiser le **score de criticité des logements par département** à partir de données stockées dans une base MongoDB. Il comprend deux visualisations principales :  
- Une **carte interactive** des scores.
- Un **histogramme** des départements les plus critiques.

## 🗂️ Contenu du projet

- `carte_criticite.py` : génère une **carte choroplèthe interactive** avec Plotly, représentant le score de criticité des logements par département.
- `Depart_score_eleve.py` : affiche un **graphique en barres** des départements avec un score de criticité élevé (entre 50 et 70).
- `Data_Logement_departement.json` : données associées aux départements, y compris noms et codes.
- `config.py` (non fourni ici) : contient la fonction `get_db()` pour se connecter à MongoDB.

## 🛠️ Prérequis

Assurez-vous d’avoir installé les bibliothèques suivantes :

```bash
pip install pandas numpy matplotlib seaborn plotly pymongo
```

Et que votre fichier `config.py` est correctement configuré :

```python
# Exemple de config.py
from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["nom_de_votre_base"]
    return db, client
```

## 📍 Visualisations

### Carte Choroplèthe (`carte_criticite.py`)
Affiche une carte interactive colorée selon le niveau de criticité des logements par département.

- Données récupérées depuis MongoDB.
- Nettoyage et filtrage des champs nécessaires.
- Utilisation d’un fichier GeoJSON pour les départements français.
- Affichage dans le navigateur via Plotly.

### Histogramme (`Depart_score_eleve.py`)
Affiche les **5 départements les plus critiques** :
- Score compris entre 50 et 70.
- Barres rouges avec les scores affichés.

## 🧪 Exemple de résultat

- 📌 Carte avec couleurs allant de jaune à rouge selon le niveau de criticité.
- 📊 Barres horizontales montrant les scores les plus élevés.

## 🔌 Connexion aux données

Les données sont chargées depuis une **base MongoDB** via `get_db()`. Assurez-vous que la collection `logements` contient les champs suivants :
- `code_departement`
- `nom_departement`
- `score_criticite`
- `priorite`

## 📁 Données JSON

Le fichier `Data_Logement_departement.json` peut être utilisé comme référence pour enrichir ou vérifier les noms/codes des départements.

## 📄 Licence

Ce projet est libre d’utilisation pour des usages académiques ou exploratoires. Attribution bienvenue 🙌