
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from config import get_db
import pandas as pd
import numpy as np
db,client= get_db()
collection = db['logements']
# === 2. Charger les données Mongo dans un DataFrame pandas ===
# On suppose que chaque document est une ligne avec tous les champs nécessaires
cursor = collection.find({})
df = pd.DataFrame(list(cursor))

# Nettoyage si besoin (_id de MongoDB)
if '_id' in df.columns:
    df.drop('_id', axis=1, inplace=True)

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from config import get_db  # Assure-toi que ce fichier contient bien ta fonction de connexion
import pandas as pd
import numpy as np

# === 1. Connexion à MongoDB ===
db, client = get_db()
collection = db['logements']

# === 2. Charger les données Mongo dans un DataFrame pandas ===
cursor = collection.find({})
df = pd.DataFrame(list(cursor))

# === 3. Nettoyage des données ===
if '_id' in df.columns:
    df.drop('_id', axis=1, inplace=True)

# === 4. Visualisation : Histogramme taux de pauvreté par département ===
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df.sort_values('taux_de_pauvrete_en', ascending=False),
    x='nom_departement',
    y='taux_de_pauvrete_en',
    palette='Reds_r'
)
plt.title('Taux de pauvreté par département')
plt.xlabel('Département')
plt.ylabel('Taux de pauvreté (%)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



