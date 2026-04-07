


def mostrar_inventario(productos):
    for num_articulo in range (len(productos)):
        print(productos[num_articulo]["nombre"])
        print(productos[num_articulo]["precio"])
        print(productos[num_articulo]["cantidad"])

        #forma 2
        for num_articulo in range (len(productos)):
           articulo= productos[num_articulo]["nombre"]+ " - " + productos[num_articulo]["precio"] + " - " + productos[num_articulo]["cantidad"]

        #forma 3
        for num_articulo in range (len(productos)):
            print(f"{productos[num_articulo]['nombre']} - str({productos[num_articulo]['precio']}) - str({productos[num_articulo]['cantidad']})")


            #forma 4
            for num_articulo in range (len(productos)):
                print (productos[num_articulo]["nombre"], end= "-")
                print (productos[num_articulo]["precio"], end= "-")
                print (productos[num_articulo]["cantidad"])

productos= []

while True:
    nombre=  input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre ==  "fin":

        mostrar_inventario(productos)
        break
precio= float(input("Ingrese el precio del producto: "))
cantidad= int(input("Ingrese la cantidad del producto: "))

productito = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}
productos.append(productito)

