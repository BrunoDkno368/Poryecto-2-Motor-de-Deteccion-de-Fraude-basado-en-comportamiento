def exportar_reporte (df, ruta):
    columnas_auditoria = [
        'id_cliente',
        'fecha',
        'monto',
        'z_score',
        'conteo_1h',
        'score',
        'es_fraude'
    ]
    df[columnas_auditoria].to_csv(ruta, index=False)


# Exporta solo columnas relevantes para:

# Auditoría

# Compliance

# Investigación manual

# Esto es exactamente lo que piden áreas de AML / Risk.

