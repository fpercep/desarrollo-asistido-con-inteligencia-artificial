import pandas as pd

ventas = {
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor'],
    'precio_base': [800, 20, 45, 200],
    'cantidad': [1, 3, 2, 1]
}
df = pd.DataFrame(ventas)

# Crear subtotales
df['subtotal'] = df['precio_base'] * df['cantidad']
df['iva'] = df['subtotal'] * 0.21
df['total'] = df['subtotal'] * df['iva']

def clasicar(precio):
    if precio < 50:
        return 'Economico'
    elif precio < 300:
        return 'Medio'
    else:
        return 'Premium'

df['categoria_precio'] = df["precio_base"].apply(clasicar)
print(df)