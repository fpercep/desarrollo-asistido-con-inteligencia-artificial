import numpy as np

np.random.seed(42)  # Para reproducibilidad

# a) Crear datos de sensores (10 sensores, 24 horas)
datosSensores = np.random.uniform(low=15, high=35, size=(10, 24))

# b) Estadísticas por sensor
media_sensor = np.mean(datosSensores, axis=1)
max_sensor = np.max(datosSensores, axis=1)
min_sensor = np.min(datosSensores, axis=1)

# c) Temperatura media por hora
media_hora = np.mean(datosSensores, axis=0)

# d) Horas críticas (>30°C)
horas_criticas = np.where(media_hora > 30)

# e) Sensor más estable
desv_sensor = np.std(datosSensores, axis=1)
sensor_mas_estable = np.argmin(desv_sensor)

# f) Sensor más variable
sensor_menos_estable = np.argmax(desv_sensor)

# g) Matriz de alertas
alertas = datosSensores > 32

# h) Alertas por sensor
alertas_sensor = np.sum(alertas, axis=1)

# i) Normalización Min-Max por sensor


# j) Rango horario (max-min por hora)
rango_horario = np.max(datosSensores, axis=0) - np.min(datosSensores, axis=0)
