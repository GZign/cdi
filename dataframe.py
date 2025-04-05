import pandas as pd
import os

# Carpetas a recorrer
carpetas = ["L1", "L2"]
dataframes = {}

# Recorremos ambas carpetas
for carpeta in carpetas:
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".csv"):
            path = os.path.join(carpeta, archivo)
            nombre_base = os.path.splitext(archivo)[0].lower()

            print(f"\n📄 Leyendo: {path}")
            df = pd.read_csv(path)

            # Guardamos el DataFrame en un diccionario para uso posterior
            dataframes[f"{carpeta}_{nombre_base}"] = df

            # Análisis básico
            print("🔍 Columnas:", df.columns.tolist())
            print("📌 Primeras filas:")
            print(df.head(3))
            print("📊 Descripción:")
            print(df.describe(include='all'))
            print("❓ Nulos:")
            print(df.isnull().sum())

# Ejemplo de uso posterior: acceder a books de L1
# df_books_L1 = dataframes["L1_books_data"]
