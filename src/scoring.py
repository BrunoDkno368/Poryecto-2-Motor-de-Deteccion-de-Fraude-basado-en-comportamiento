from src.config import UMBRAL_SCORE_FRAUDE

def calcular_score(df):
    df['score']= (
        df['flag_monto_anomalo'] * 40 +
        df['flag_rafaga']*30 +
        df['flag_horario_nocturno'] *20
    )

    df['es_fraude'] = df['score']>= UMBRAL_SCORE_FRAUDE

    return df

# Construye un score ponderado (modelo experto rule-based).