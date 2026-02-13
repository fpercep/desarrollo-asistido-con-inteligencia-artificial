import pandas as pd

ventas = {
    'producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Webcam', 'Auriculares'],
    'categoria': ['Informática', 'Accesorios', 'Informática', 'Accesorios', 'Accesorios', 'Accesorios'],
    'precio': [800, 20, 200, 45, 60, 35],
    'cantidad': [5, 30, 8, 15, 12, 20]
}

df = pd.DataFrame(ventas)
df['subtotal'] = df['precio'] * df['cantidad']

resultado = df.groupby('categoria').agg({'subtotal': 'sum', 'precio': 'mean', 'producto': 'count'})
masIngresos = resultado.sort_values('subtotal', ascending=False).head(1)
masVentas = df.sort_values('cantidad', ascending=False).head(1)
print(masIngresos)
print()
print(masVentas)
