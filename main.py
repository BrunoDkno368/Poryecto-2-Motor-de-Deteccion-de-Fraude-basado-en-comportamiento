from src.auditoria import exportar_reporte
from src.config import RUTA_OUTPUT, RUTA_RAW
from src.features import calcular_z_score, calculta_estadistica_cliente, detectar_rafaga
from src.generador_datos import generar_transacciones
from src.regla_fraude import aplicar_reglas
from src.scoring import calcular_score

def main():
    print("==============INICIO DEL PROCESO===============")
    print("Generando Datos")
    df= generar_transacciones()
    print("Calculando estadistica")
    df= calculta_estadistica_cliente(df)
    print("Calculando Z score")
    df= calcular_z_score(df)
    print("Detectamos rafaga")
    df= detectar_rafaga(df)
    print("Aplicando Reglas")
    df= aplicar_reglas(df)
    print("Calculando score")
    df= calcular_score(df)

    # print("Resumen score:")
    # print(df["score"].describe())

    # print("Distribución es_fraude:")
    # print(df["es_fraude"].value_counts())

    print("Exportando datos")
    exportar_reporte(df, RUTA_OUTPUT)
    print("==============PROCESO FINALIZADO================")


if __name__ == "__main__":
    main()
# Este proyecto comunica:

# Diseño modular

# Pensamiento estadístico

# Arquitectura escalable

# Enfoque auditoría/compliance

# Capacidad de producción

# Mentalidad bancaria real

# Esto ya es perfil serio de:

# Fraud Risk Analyst

# Risk Scoring Analyst

# AML Monitoring Analys