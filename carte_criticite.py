import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
from config import get_db
import pandas as pd
import numpy as np

# Affichage dans le navigateur
pio.renderers.default = 'browser'

# Connexion à la base
db, client = get_db()
collection = db['logements']

# Chargement des données
cursor = collection.find({})
df = pd.DataFrame(list(cursor))

# Nettoyage
if '_id' in df.columns:
    df.drop('_id', axis=1, inplace=True)

# Supprimer les lignes avec données manquantes importantes
df = df.dropna(subset=['code_departement', 'score_criticite', 'nom_departement'])

# Carte interactive stylisée
fig = px.choropleth(
    df,
    geojson='https://france-geojson.gregoiredavid.fr/repo/departements.geojson',
    locations='code_departement',
    featureidkey="properties.code",
    color='score_criticite',
    hover_name='nom_departement',
    title='Score de criticité des logements par département',
    color_continuous_scale='YlOrRd',
)

# Mise en forme
fig.update_geos(
    fitbounds="locations",
    visible=False,
    showland=True,
    landcolor="lightgray",
    showcoastlines=False,
    showlakes=False
)

fig.update_layout(
    title={
        'text': "Carte du score de criticité des logements par département",
        'x': 0.5,
        'xanchor': 'center',
        'font': dict(size=22)
    },
    coloraxis_colorbar=dict(
        title="Score",
        tickvals=np.linspace(df['score_criticite'].min(), df['score_criticite'].max(), 6).round(2),
        len=0.75
    ),
    margin={"r":0,"t":50,"l":0,"b":0},
)

fig.show()

