from src.config import UMBRAL_Z_SCORE, UMBRAL_TRANSACCIONES_RAFAGA

def aplicar_reglas(df): 
    df['flag_monto_anomalo'] = df['z_score'].abs()> UMBRAL_Z_SCORE
    df['flag_rafaga'] = df['conteo_1h'] > UMBRAL_TRANSACCIONES_RAFAGA

    df['flag_horario_nocturno'] =df['fecha'].dt.hour.isin(range(0,6))
    return df 
    
# Convierte métricas estadísticas en señales binarias de riesgo.