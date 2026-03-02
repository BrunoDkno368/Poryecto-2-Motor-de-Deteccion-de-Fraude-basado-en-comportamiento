🚀 Proyecto 2 – Motor de Detección de Fraude Basado en Comportamiento

📌 Descripción


Este es mi segundo proyecto enfocado en Fraud Detection y Risk Scoring, donde evoluciono desde un sistema basado en reglas simples hacia un motor de scoring conductual capaz de evaluar riesgo de manera acumulativa y parametrizable.

El objetivo del proyecto es diseñar un sistema que:

Analice transacciones financieras

Detecte patrones sospechosos

Asigne un nivel de riesgo cuantitativo

Clasifique posibles fraudes en función de un umbral configurable

Este motor simula la lógica base utilizada en sistemas antifraude de banca y fintech.

🎯 Objetivo del Proyecto

Desarrollar un modelo heurístico de scoring de riesgo que permita:

Evaluar múltiples señales simultáneamente

Combinar comportamiento transaccional en un score único

Permitir calibración del nivel de sensibilidad

Generar una arquitectura modular y escalable

El sistema no solo responde “sí o no”, sino que modela el riesgo acumulado de cada operación.

🧠 Enfoque Conceptual

El proyecto implementa:

Feature Engineering

Detección de monto anómalo

Análisis de ráfaga de transacciones (velocity check)

Evaluación de operaciones en horario nocturno

Modelo de Scoring Ponderado

Combinación lineal de señales

Asignación de pesos según severidad

Generación de un score continuo de riesgo

Clasificación por Umbral

Separación entre evaluación de riesgo y decisión final

Umbral configurable

Simulación de distintos niveles de sensibilidad

⚙️ Arquitectura del Sistema

Transacciones
↓
Feature Engineering (Flags)
↓
Cálculo de Score
↓
Aplicación de Umbral
↓
Clasificación (es_fraude)

Esta estructura permite:

Escalabilidad

Fácil ajuste de pesos

Extensión a nuevos indicadores

Evolución futura hacia Machine Learning supervisado

📊 Resultado

El sistema:

Genera un score de riesgo para cada transacción

Permite analizar la distribución de riesgo

Identifica operaciones con mayor probabilidad de fraude

Simula un motor antifraude basado en comportamiento

Este proyecto representa una mejora estructural respecto al Proyecto 1, pasando de reglas aisladas a un modelo cuantitativo de evaluación de riesgo.

🛠 Stack Tecnológico

Python

Pandas

Análisis de datos

Modelado heurístico

Arquitectura modular

📈 Evolución desde el Proyecto 1
Proyecto 1	Proyecto 2
Reglas simples	Scoring acumulativo
Lógica binaria	Modelo cuantitativo
Condición aislada	Múltiples señales combinadas
Estructura básica	Arquitectura modular

Este proyecto marca el paso hacia sistemas más robustos y cercanos a modelos de Machine Learning aplicados a fraude.

👤 Autor

Argañaraz Bruno
Interesado en Fraud Detection, Risk Modeling, Data Analytics y soluciones antifraude en banca y fin
