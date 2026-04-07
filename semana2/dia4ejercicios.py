total=0

for articulo in range(4):
    desea_comprar = input("desea comprar? (si/no): ")
    if desea_comprar == "si":
        precio = float(input("Ingrese el precio del articulo: "))
        total += precio
