    
def calcular_valor(producto):
    return producto[1] * producto[2]

inventario = [
    ["Croquetas", 15, 20, 0],
    ["Juguete", 10, 5, 0],
    ["Champu", 5, 12, 0]
]


for producto in inventario:
    producto[3] = calcular_valor(producto)

print(">>> SISTEMA DE GESTION HUELLITAS FELICES <<<")


while True:
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for producto in inventario:
        print(producto[0], "| Stock:", producto[1], "| Precio:", producto[2])

    print("\nOpciones: vender / agregar / eliminar / salir")
    opcion = input("Elija una opcion: ")

    
    if opcion == "salir":
        break

   
    elif opcion == "vender":
        nombre = input("Nombre del producto: ")
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

    
    elif opcion == "agregar":
        nombre = input("Nombre del nuevo producto: ")
        cantidad = int(input("Cantidad: "))
        precio = int(input("Precio: "))

        nuevo = [nombre, cantidad, precio, 0]
        nuevo[3] = calcular_valor(nuevo)

        inventario.append(nuevo)
        print("Producto agregado")

   
    elif opcion == "eliminar":
        nombre = input("Nombre del producto a eliminar: ")
        encontrado = False

        for eliminado in range(len(inventario)):
            if inventario[eliminado][0] == nombre:
                inventario.pop(eliminado)
                encontrado = True
                print("Producto eliminado")
                break

        if encontrado == False:
            print("Producto no existe")


print("\n>>> RESUMEN FINAL HUELLITAS FELICES <<<")

total = 0

for producto in inventario:
    print(producto[0], "| Stock:", producto[1], "| Precio:", producto[2], "| Valor:", producto[3])
    total = total + producto[3]

print("TOTAL GENERAL:", total)



