import numpy as np

ventas = np.array([
    [1000, 1200, 1100, 1300],
    [900, 1000, 950, 1050],
    [1500, 1600, 1550, 1700]
])

# a) Shape
print(f"a) shape: {ventas.shape}")

# b) Ventas Tienda 2
tienda_2 = ventas[1, :]
print(f"b) Ventas Tienda 2: {tienda_2}")

# c) Ventas Trimestre 3
trimestre_3 = ventas[:, 2]
print(f"c) Ventas Tienda 2: {trimestre_3}")

# d) Total por tienda (suma por filas)
total_tiendas = ventas.sum(axis=1)
print(f"d) Total Tiendas: {total_tiendas}")

# e) Total por trimestre (suma por columnas)
total_trimestre = ventas.sum(axis=0)
print(f"e) Total Trimestre: {total_trimestre}")

# f) Media por tienda
media_tienda = ventas.mean(axis=1)
print(f"f) Media Tienda: {media_tienda}")

# g) Tienda con mayores ventas
mayor_tienda = np.argmax(total_tiendas)
print(f"g) Mejor Tienda: {mayor_tienda}")

# h) Trimestre con menores ventas
menor_tienda = np.argmin(total_trimestre)
print(f"h) Menor Trimestre: {menor_tienda}")