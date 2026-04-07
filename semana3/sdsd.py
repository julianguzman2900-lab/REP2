# Función para calcular valor total
def calcular_valor(producto):
    return producto[1] * producto[2]

# Inventario
inventario = [
    ["Croquetas", 15, 20, 0],
    ["Juguete", 10, 5, 0],
    ["Champu", 5, 12, 0]
]

# Calcular total invertido
total = 0
for producto in inventario:
    producto[3] = calcular_valor(producto)
    total = total + producto[3]

print("Total invertido:", total)

# Mostrar productos
print("\nProductos disponibles:")
for producto in inventario:
    print(producto[0], "| Stock:", producto[1], "| Precio:", producto[2])

# Venta
while True:
    nombre = input("\nNombre del producto (o salir): ")

    if nombre == "salir":
        break

    encontrado = False

    for producto in inventario:
        if producto[0] == nombre:
            encontrado = True

            cantidad = int(input("Cantidad: "))

            if cantidad <= producto[1]:
                producto[1] = producto[1] - cantidad
                producto[3] = calcular_valor(producto)
                print("Venta realizada")
            else:
                print("No hay suficiente stock")

    if encontrado == False:
        print("Producto no existe")

# Mostrar inventario final
print("\nInventario final:")
for producto in inventario:
    print(producto)

# Total final
total_final = 0
for producto in inventario:
    total_final = total_final + producto[3]

print("Total final:", total_final)