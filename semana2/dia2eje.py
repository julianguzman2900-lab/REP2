print("CAJAS DE LECHE DISPONIBLES EN INVENTARIO")

cajas_disponibles=int(input("Ingrese el número de cajas de leche disponibles en el inventario   : "))
if cajas_disponibles>20:
    print("-----------------------------")
    print("El inventario es saludable")
    print("-----------------------------")

elif cajas_disponibles >0:
    print("----------------------------------------")
    print("ALERTA: REALIZE UN PEDIDO A SU PROVEEDOR")
    print("----------------------------------------")

else:
    print("-----------------------------------")
    print("URGENTE: EL PRODUCTO ESTA AGOTADO")
    print("-----------------------------------")