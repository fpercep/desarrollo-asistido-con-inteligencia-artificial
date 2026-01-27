# 1.Análisis de ventas

ventas = [15000, 18000, 22000, 17000, 25000, 30000, 28000, 32000, 27000, 29000, 35000, 40000]
total_ventas = sum(ventas)

def calcular_estadisticas(lista):
    total = sum(lista)
    promedio = total / len(lista)

    mes_mejor = lista.index(max(lista))
    mes_peor = lista.index(min(lista))

    return total, promedio, mes_mejor, mes_peor

resultado = calcular_estadisticas(ventas)

#Esta fue mi solución, pero tenia el problema de que si se repentian valores imprimia dos veces la primera ocurrencia
#ventas_mayor_promedio = [venta for venta in ventas if venta > resultado[1]]
#for venta in ventas_mayor_promedio:
#    print("Mes" + str(ventas.index(venta) + 1) + ": €" + str(venta))

#La IA me explica sobre enumerate(), que te permite sacar clave-valor. Ademas me recomendo guardar el string directamente
ventas_top = [f"Mes {i}: €{v}" for i, v in enumerate(ventas) if v > resultado[1]]
print("Ventas que superaron el promedio:", ventas_top)

ventas_inflacion = list(map(lambda x: x*1.15, ventas))
ventas_fitradas = list(filter(lambda x: x>30000, ventas_inflacion))
print(f"Ventas superiores a 30000 pos inflación: {ventas_fitradas}")


# 2.Gestión de inventario
productos = {
    "laptop": {"precio": 850, "stock": 15, "categoria": "informatica"},
    "raton": {"precio": 25, "stock": 50, "categoria": "informatica"},
    "teclado": {"precio": 45, "stock": 30, "categoria": "informatica"},
    "monitor": {"precio": 200, "stock": 20, "categoria": "informatica"},
    "silla": {"precio": 150, "stock": 10, "categoria": "mobiliario"},
    "mesa": {"precio": 300, "stock": 5, "categoria": "mobiliario"}
}

def valor_total_inventario(p):
    total = 0
    for valor in p.values():
        total += (valor["precio"] * valor["stock"])
    return total

def productos_por_categoria(p,c):
    output = {}
    for indice, valor in p.items():
        if valor["categoria"] == str(c):
            output[indice] = valor
    return output

productos_bajo_stock = {nombre: info["stock"] for nombre, info in productos.items() if info["stock"] < 20}


def actualizar_precios(dicc_productos, porcentaje):
    output = []
    factor = 1 + (porcentaje / 100)

    for nombre, info in dicc_productos.items():
        info["precio"] = info["precio"] * factor
        if info["precio"] > 200:
            output.append(nombre)

    return output

import numpy as np

np.random.seed(42)
temperaturas = np.random.uniform(15, 35, size=(5, 7))

print(f"Shape: {temperaturas.shape}")
print(f"Media global: {np.mean(temperaturas)}")
print(f"Máximo: {np.max(temperaturas)}, Mínimo: {np.min(temperaturas)}")

media_sensor = np.mean(temperaturas, axis=1)
media_dia = np.mean(temperaturas, axis=0)
sensor_mas_caluroso = np.argmax(media_sensor)

print(f"Media por sensor: {media_sensor}")
print(f"Índice sensor con mayor media: {sensor_mas_caluroso}")

ajuste_mask = temperaturas > 28
num_ajustados = np.sum(ajuste_mask)
temperaturas[ajuste_mask] = 28
print(f"Valores ajustados a 28°C: {num_ajustados}")

t_min = np.min(temperaturas)
t_max = np.max(temperaturas)
temperatura_normalizada = (temperaturas - t_min) / (t_max - t_min)
print("Primeras 3 filas normalizadas:\n", temperatura_normalizada[:3])

alertas = np.array([10, 20, 15, 25, 18])
alertas_reshaped = alertas.reshape(5, 1)
resultado_alertas = temperaturas + alertas_reshaped
print(f"Resultado tras alertas (Broadcasting):\n{resultado_alertas}")


np.random.seed(123)
calificaciones = np.random.uniform(4, 10, size=(20, 5))
calificaciones = np.round(calificaciones, 1)

asignaturas = ["Matemáticas", "Física", "Programación", "Inglés", "Historia"]

def estudiantes_aprobados(matriz, nota_minima=5.0):
    # np.all comprueba si todos los elementos de la fila cumplen la condición
    aprobados_bool = np.all(matriz >= nota_minima, axis=1)
    num_aprobados = np.sum(aprobados_bool)
    indices = np.where(aprobados_bool)[0]
    return aprobados_bool, num_aprobados, indices

_, cantidad, indices_aprobados = estudiantes_aprobados(calificaciones)
print(f"Estudiantes que aprobaron todo: {cantidad}. Índices: {indices_aprobados}")

medias_asig = np.mean(calificaciones, axis=0)
mejor_asig = asignaturas[np.argmax(medias_asig)]
peor_asig = asignaturas[np.argmin(medias_asig)]
std_asig = np.std(calificaciones, axis=0)

print(f"Asignatura con mejor media: {mejor_asig}")
print(f"Asignatura con más variabilidad: {asignaturas[np.argmax(std_asig)]}")

media_estudiantes = np.mean(calificaciones, axis=1)

condiciones = [
    media_estudiantes >= 9,
    (media_estudiantes >= 7) & (media_estudiantes < 9),
    (media_estudiantes >= 6) & (media_estudiantes < 7),
    (media_estudiantes >= 5) & (media_estudiantes < 6)
]
opciones = ["Excelente", "Notable", "Bien", "Aprobado"]
clasificacion = np.select(condiciones, opciones, default="Suspenso")
print(f"5 primeros: {clasificacion[:5]}")

top_estudiantes_idx = np.argmax(calificaciones, axis=0)

matriz_dif = calificaciones - medias_asig

dif_positivas = np.where(matriz_dif > 0, matriz_dif, 0)
suma_dif_pos = np.sum(dif_positivas, axis=1)
estudiante_estrella = np.argmax(suma_dif_pos)
