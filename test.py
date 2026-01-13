import pandas as pd

# CSV einlesen (Header wird automatisch erkannt)
df = pd.read_csv('tournament_standings.csv')

# Erste 15 Datenzeilen entfernen (Header bleibt erhalten)
df = df.iloc[12:]

# Index zurücksetzen und Nummerierung anpassen
df = df.reset_index(drop=True)

# Speichern (ohne zusätzlichen Index)
df.to_csv('tournament_standings_2.csv', index=False)