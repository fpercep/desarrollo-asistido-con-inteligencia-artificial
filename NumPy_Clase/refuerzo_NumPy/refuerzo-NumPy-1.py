import numpy as np

# a) Array del 0 al 9
rango = np.arange(10)

# b) Array 3x4 de ceros
zeros = np.zeros((3,4))

# c) Array 2x5 de unos
ones = np.ones((2,5))

# d) Matriz identidad 4x4
eye = np.eye(4)

# e) Explorar propiedades de cada array

print(f"------------- Array del 0 al 9 ------------")
print(f"Forma (shape): {rango.shape}")
print(f"Dimensiones: {rango.ndim}")
print(f"Tamaño total: {rango.size}")
print(f"Tipo de datos: {rango.dtype}")
print(f"---------------------------------------------")

print(f"------------- Array 3x4 de ceros ------------")
print(f"Forma (shape): {zeros.shape}")
print(f"Dimensiones: {zeros.ndim}")
print(f"Tamaño total: {zeros.size}")
print(f"Tipo de datos: {zeros.dtype}")
print(f"---------------------------------------------")

print(f"------------- Array 2x5 de unos ------------")
print(f"Forma (shape): {ones.shape}")
print(f"Dimensiones: {ones.ndim}")
print(f"Tamaño total: {ones.size}")
print(f"Tipo de datos: {ones.dtype}")
print(f"---------------------------------------------")

print(f"------------- Matriz identidad 4x4 ------------")
print(f"Forma (shape): {eye.shape}")
print(f"Dimensiones: {eye.ndim}")
print(f"Tamaño total: {eye.size}")
print(f"Tipo de datos: {eye.dtype}")
print(f"---------------------------------------------")