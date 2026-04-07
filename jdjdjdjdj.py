def calcular_valor(producto):
    return producto[1] * producto[2]

inventario = [
    ["croquetas", 15, 20, 0],
    ["juguete", 10, 5, 0],
    ["champu", 5, 12, 0]
]



total=0
for producto in inventario:
    producto[3]= calcular_valor(producto)
    total+=producto[3]

print(">>> SISTEMA DE GESTION HUELLITAS FELICES<<<")

while True:
    print("\n----PRODUCTOS DISPONIBLES----")
    for producto in inventario:
        print(producto[0],  "|Stock:", producto[1], "|precio:", producto[2])

    print("\Que desea hacer?: vender / agregar / eliminar /salir")
    opcion= input("Elija una opcion: ")


    if opcion== "salir": 
        break

    elif opcion== "vender":
        nombre =input("ingrese el nombre del producto: ")
        encontrado= False 
        for producto in inventario:
            if producto[0]== nombre:
                encontrado= True
                cantidad = int(input("cantidad:"))

                if cantidad <=producto [1]:
                    producto[1]= producto[1]- cantidad
                    producto[3]= calcular_valor(producto)
                    print("Venta realizada")

                else:
                    print("No hay suficiente stock")

        if encontrado == False:
            print("Producto no existe")


    

    elif opcion == "eliminar":
        nombre=input("Ingrese el nombre del producto a eliminar: ")
        encontrado= False
    for eliminado in range(len(inventario)):
            if inventario[eliminado][0]== nombre:
                inventario.pop(eliminado)
                encontrado= True
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