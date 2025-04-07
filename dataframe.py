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

            # Configura separador y encoding según el tipo
            if carpeta == "L1":
                sep = ','
                encoding = 'utf-8'
            else:  # L2
                sep = ';'
                encoding = 'ISO-8859-1'

            try:
                df = pd.read_csv(path, sep=sep, encoding=encoding)
            except Exception as e:
                print(f"⚠️ Error al leer {path}: {e}")
                continue

            # Guardamos el DataFrame en un diccionario
            dataframes[f"{carpeta}_{nombre_base}"] = df

            # Análisis básico
            print("🔍 Columnas:", df.columns.tolist())
            print("📌 Primeras filas:")
            print(df.head(3))
            print("📊 Descripción:")
            print(df.describe(include='all'))
            print("❓ Nulos:")
            print(df.isnull().sum())
