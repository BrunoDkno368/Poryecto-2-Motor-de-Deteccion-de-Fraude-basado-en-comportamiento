import pandas as pd 
import numpy as np 
# from config import NUM_CLIENTES, NUM_TRANSACCIONES
from datetime import datetime, timedelta

def generar_transacciones(NUM_CLIENTES= 100, NUM_TRANSACCIONES= 5000):
    np.random.seed(42)

    clientes = np.random.randint(1, NUM_CLIENTES+1, NUM_TRANSACCIONES)
    monto = np.random.exponential(scale=200, size=NUM_TRANSACCIONES)

    fechas = [
        datetime.now() -timedelta(minutes=np.random.randint(0,60*24*30))
        for _ in range (NUM_TRANSACCIONES)
    ]
    paises = np.random.choice(['Argentina','Brasil', 'Chile'], NUM_TRANSACCIONES)

    df= pd.DataFrame({
        'id_cliente' : clientes,
        'monto': monto,
        'fecha': fechas,
        'pais': paises

    })

    return df

# Distribución exponencial (monto)

# Ventana temporal de 30 días

# País como variable geográfica