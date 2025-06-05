import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from config import get_db
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from IPython.display import display
db,client= get_db()
collection = db['logements']
# === 2. Charger les données Mongo dans un DataFrame pandas ===
# On suppose que chaque document est une ligne avec tous les champs nécessaires
cursor = collection.find({})
df = pd.DataFrame(list(cursor))

# Nettoyage si besoin (_id de MongoDB)
if '_id' in df.columns:
    df.drop('_id', axis=1, inplace=True)
# Filtre des départements "Élevée"
df_Eleve = df[
    (df['priorite'] == 'Elevée') | 
    (df['score_criticite'].between(50, 70))
].sort_values('score_criticite', ascending=False)

# Préparation des données
df_Eleve= df_Eleve.head(5)  # Top 2

# 3. Création de l'histogramme
plt.figure(figsize=(10, 6))
bars = plt.barh(
    df_Eleve['nom_departement'],
    df_Eleve['score_criticite'],
    color="#FF0000",  # Orange pour "Elevée"
    height=0.6
)

# 4. Personnalisation
plt.title('Départements avec Score de Criticité Élevé (50-70)', pad=20)
plt.xlabel('Score de criticité', labelpad=10)
plt.xlim(0, 100)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 5. Ajouter les valeurs sur les barres
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 1,  # Décalage à droite de la barre
        bar.get_y() + bar.get_height()/2,
        f'{width:.1f}',
        va='center',
        fontsize=10
    )
plt.tight_layout()
plt.show()



