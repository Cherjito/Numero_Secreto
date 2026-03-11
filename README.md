# Predicción Estadística basada en Datos Históricos mediante análisis de KPIs

Este proyecto consiste en un simulador desarrollado en **Python** diseñado para evaluar procesos de negocio mediante la generación de valores aleatorios, el almacenamiento de datos históricos y el cálculo de métricas estadísticas de rendimiento.

## Aplicación en Entornos de Negocio
Aunque el script utiliza una lógica de "número secreto" para la ejecución técnica, el modelo es **totalmente escalable**. La variable `numero_secreto` puede ser sustituida fácilmente por indicadores críticos de gestión como:
* **Objetivos de Facturación:** Evaluar la probabilidad de alcanzar una cifra de ventas.
* **Cuotas de Ventas:** Simular escenarios de demanda por producto.
* **En el apartado de:** "Escribe un número del 1 al 100" se podria poner algo como "Escribe las ventas/facturación de hoy" y con eso devolver algo como "El objetivo de diario no/si se ha cumplido" y calcular estadisticos que nos ayuden a preveer la probabilidad de que la facturación en un dia futuro sea mayor, menor o igual a un objetivo preestablecido

## Funcionalidades Principales

* **Persistencia de Datos (CSV):** Implementación de la librería `csv` para registrar cada interacción. Esto permite generar una base de datos histórica acumulativa.
* **Cálculo de KPIs Operativos:** El sistema lee el histórico y procesa automáticamente:
    * **Promedio de intentos:** Coste operativo medio para alcanzar el éxito.
    * **Métricas Extremas:** Identificación de mejores y peores desempeños registrados.
    * **Tasa de éxito directo:** Eficiencia porcentual basada en aciertos al primer intento.
* **Modelado Probabilístico:** Uso de la **Distribución de Bernoulli** para prever la probabilidad real de éxito y fracaso basada en la experiencia previa.
* **Gestión de Excepciones:** Control de errores mediante bloques `try-except` para garantizar la estabilidad operativa frente a archivos inexistentes o corruptos.

##  Cómo ejecutar el programa
1. Asegúrate de tener instalado **Python 3.x**.
2. Descarga el archivo `.py` y ejecútalo en tu terminal.
3. El programa generará automáticamente un archivo `resultados.csv` en la misma carpeta para almacenar los datos.

##  Ejemplo de Salida en Terminal (datos inventados solo para mostrar ejemplo de salida)
Al finalizar cada ejecución, el programa arroja un análisis detallado:
- "Promedio de intentos: 4.2"
- "Número de éxitos directos: 2"
- "Probabilidad de éxito Bernoulli P (acertar a la primera): 20%"
- "Probabilidad de fracaso 1-p: 80%
- "El mejor resultado es Sergio con 1 intentos"
- "El peor resultado es Javi con 23 intentos"
- "El promedio de fracasos antes del exito es de:3"
- "De 10 usuarios, 2 acertaron a la primera"

---
Desarrollado por **Sergio Ruiz Gutiérrez** como parte de mi enfoque en Análisis de Datos y Logística.
