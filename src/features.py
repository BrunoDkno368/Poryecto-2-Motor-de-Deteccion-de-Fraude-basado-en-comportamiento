import pandas as pd 
import numpy as np 

def calculta_estadistica_cliente (df):
    stats = df.groupby('id_cliente')['monto'].agg(['mean','std']).reset_index()
    stats.columns= ['id_cliente', 'media_cliente', 'desviacion_cliente']
    return df.merge(stats, on='id_cliente')


def calcular_z_score (df):
    df['z_score'] = (df['monto']- df['media_cliente'])/ df['desviacion_cliente']
    return df

def detectar_rafaga(df):

    df = df.sort_values(["id_cliente", "fecha"])

    # Aseguramos que fecha sea datetime
    df["fecha"] = pd.to_datetime(df["fecha"])

    # Aplicamos rolling correctamente manteniendo índice
    df["conteo_1h"] = (
        df.groupby("id_cliente")
          .apply(lambda x: x.set_index("fecha")
                             .rolling("60min")["monto"]
                             .count())
          .reset_index(level=0, drop=True)
          .reset_index(drop=True)
    )

    return df
# calcular_estadisticas_cliente → calcula baseline individual

# calcular_zscore → mide desviación individual

# detectar_rafaga → detecta alta frecuencia en ventana móvil

# Esto ya es nivel banca real.