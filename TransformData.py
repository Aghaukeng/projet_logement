from config import get_db
import pandas as pd
import numpy as np
db,client= get_db()
collection = db['logements']
count = collection.count_documents({})
# Je procede au nettoyage de mes données afin de recenser les variables qui seront utiles pour notre analyse 
# Chargement des données
df= pd.read_json ('Data_Logement_departement.json')  # Adaptez le séparateur si nécessaire
# Liste des colonnes essentielles  pour l'analyse
colonnes_utiles = [
    'code_departement',
    'nom_departement',
    'code_region',
    'nom_region',
    'taux_de_pauvrete_en',
    'nombre_de_logements',
    'taux_de_logements_sociaux_en',
    'parc_social_nombre_de_logements',
    'parc_social_age_moyen_du_parc_en_annees',
    'parc_social_taux_de_logements_energivores_e_f_g_en',
    'parc_social_loyer_moyen_en_eur_m2_mois',
    'taux_de_logements_vacants_en',
    'taux_de_logements_individuels_en'
  
]
df_clean=df[colonnes_utiles].copy()
#print(df_clean)
df_clean.to_json('Data_Logement_departement.json')

# Suppression des lignes avec données manquantes critiques
df_clean = df_clean.dropna(subset=[
    'parc_social_age_moyen_du_parc_en_annees',
    'parc_social_taux_de_logements_energivores_e_f_g_en'
])

# Calcul du score de criticité
df_clean['score_criticite'] = (
    (df_clean['parc_social_age_moyen_du_parc_en_annees'] * 0.6) + 
    (df_clean['parc_social_taux_de_logements_energivores_e_f_g_en'] * 0.4)
).round(2)

# Définition des seuils de priorité
seuils = {
    'Urgent': (70, float('inf')),      # Score > 70%
    'Elevée': (50, 70),               # 50% < Score ≤ 70%
    'Modérée': (30, 50),              # 30% < Score ≤ 50%
    'Faible': (0, 30)                  # Score ≤ 30%
}

# Attribution des libellés de priorité
df_clean['priorite'] = pd.cut(
    df_clean['score_criticite'],
    bins=[0, 30, 50, 70, float('inf')],  # Notez l'utilisation de float('inf') pour la dernière borne
    labels=['Faible', 'Modérée', 'Elevée', 'Urgent'],
    right=False  # Ce paramètre contrôle si les intervalles sont [a,b) ou (a,b]
)
# Vérification
#print(df_clean)
# Conversion du DataFrame en liste de dictionnaires
data_to_insert = df_clean.to_dict('records')

# Insertion en une seule opération
if data_to_insert:
    collection.delete_many({})  # facultatif : si tu veux "écraser" les données existantes
    collection.insert_many(data_to_insert)
    #print(f"{len(data_to_insert)} documents insérés avec succès dans MongoDB.")
else:
    print("Aucune donnée à insérer.")

#print(df_clean['priorite'].value_counts())
print(df_clean['score_criticite'].describe())
