import pandas as pd

# Création d'un DataFrame vide avec les colonnes désirées
df = pd.DataFrame(columns=['DATE_DECLARATION', 'DATE_ACHAT', 'HEURE_ACHAT', 'NUMERO_IMMAT', 'NUMERO_ID'])

# Enregistrement du DataFrame dans un fichier CSV
df.to_csv('donnees_vides.csv', index=False)

print("Le fichier CSV 'donnees_vides.csv' a été créé avec les colonnes spécifiées.")
