# Problema 3: Auditoria de inventario
# Estudiante: Maira Ramirez
# Grupo: 213022_46
# Curso: Fundamentos de Programación

"""Herramienta para auditar el inventario y 
decidir qué artículos necesitan ser reabastecidos. La información se 
encuentra en una matriz: [Código Artículo, Nombre, Stock Actual, Stock 
Mínimo Requerido]. """

"""Requisitos de Desarrollo:

Matriz: Crear una matriz con al menos 5 artículos.
Módulos: Se requiere un módulo (función) para determinar la 
cantidad exacta a pedir para un artículo.

Lógica de Negocio: 

- Si el Stock Actual es menor al Stock Mínimo, la cantidad 
a pedir es la diferencia (Mínimo Requerido - Stock Actual). 
- Si el Stock Actual es suficiente (mayor o igual al Mínimo), 
la cantidad a pedir es cero. 

- Salida: Imprimir una lista de pedidos que muestre el nombre del 
artículo y la cantidad exacta que debe ser solicitada, si la cantidad es menor que cero, se debe mostrar el artículo con cantidad cero."""

 

# Matriz de inventario: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
inventario = [
    ["A001", "Audifonos", 2, 5],
    ["A002", "Mouse", 20, 10],
    ["A003", "Teclado", 15, 8],
    ["A004", "Memoria USB", 1, 3],
    ["A005", "Tarjeta grafica", 8, 4]
]

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """Calcula la cantidad a pedir para un artículo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0
# Lista de pedidos
pedidos = []
# Evaluar cada artículo en el inventario
for articulo in inventario:
    codigo, nombre, stock_actual, stock_minimo = articulo
    cantidad_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    pedidos.append((nombre, cantidad_a_pedir))
# Imprimir la lista de pedidos
print("Lista de Pedidos:")
for nombre, cantidad in pedidos:
    print(f"Artículo: {nombre}, Cantidad a pedir: {cantidad}")
