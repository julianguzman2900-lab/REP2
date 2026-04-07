# nombre_producto= "camiseta" '''''
# precio_producto= 19.88
# cantidad_producto= 3
# descuento= True



# print("Nombre del producto: ", nombre_producto, "tipo", type(nombre_producto))
# print("Precio del producto: ", precio_producto, "tipo", type(precio_producto))
# print("Cantidad del producto: ", cantidad_producto, "tipo", type(cantidad_producto))
# print("Descuento del producto: ", descuento, "tipo", type(descuento))



# #forma 1 convertir despues de preguntar
# cantidad= input("cuantos cafes dsea comprar?")
# cantidad= int(cantidad_producto)


# #forma2 convertir directamente al pedir el input
# precio= float (input("cuel es el precio del cafe?"))
# precio= float("19.88")
# precio= 19.88

# print("cantidad de cafe:",cantidad, "tipo", type(cantidad))
# print("precio del cafe:",precio, "tipo", type(precio))


# valor1= 10
# valor2= 2
# # division normal
# resultado= valor1/valor2  # resultado es un float aunque ambos sean enteros, 3.5
# print("Resultado:", resultado, "tipo", type(resultado))

# #d`ivision entera
# resultado_entero= valor1//valor2 # resultado es un int, aunque ambos valores sean enteros , 3

# # modulo o resto de la division

# resto= valor1%valor2 # resultado es un int, aunque ambos valores sean enteros, 0
# print("resultado de la division:", resultado)
# print("resultado de la division entera:", resultado_entero)
# print("resto de la division:", resto)


# #caja registradora
# print("Bienvenido a la tienda")
# nombre_producto = input("Ingrese el nombre del producto: ")
# precio_producto = float(input("Ingrese el precio del producto: "))
# cantidad_producto = input("Ingrese la cantidad del producto: ")
# cantidad_producto = int(cantidad_producto)

# #procesamiento de la informacion

# subtotal = precio_producto * cantidad_producto
# impuesto = subtotal * 0.16
# total = subtotal + impuesto

# # impresion de resultados   

# print("\n=== RESUMEN DE LA COMPRA ===")
# print("%15s: %10s" % ("Nombre del producto", nombre_producto))
# # %s : string
# # %f : float
# # %d : int
# print("nobre del producto:", nombre_producto)
# print("precio del producto:", precio_producto)
# print("cantidad del producto:", cantidad_producto)  
# print("subtotal:", subtotal)
# print("impuesto:", impuesto)
# print("total a pagar:", total)



# print("%15s: %2f" % ("precio del producto", precio_producto))

# print("%15s: %10d" % ("cantidad del producto", cantidad_producto))

# print("%15s: %10.2f" % ("subtotal", subtotal))

# print("impuesto:", impuesto)
# print("%15s: %10.2f"%("impuesto", impuesto))
      
# print("%15s: %10.2f" %("total", total))


# ###################################################################################
# ######################################
# ############################################
# inventario= 8
# print(inventario>=8)

# print(inventario==8)

# nombre_producto1 = "camiseta"
# nombre_producto2 = "CAMISETA"
# print(nombre_producto1 == nombre_producto2)

# print(nombre_producto1 == nombre_producto)
# '''
# '''''
# manzanas=5
# precio_manzanas= 500

# print("----- REPORTE ---")

# hay_manzanas= manzanas> 10
# print("hay mas de 10 manzanas?", hay_manzanas)

# sin_stock= manzanas==0
# print("sin stock?", sin_stock)
# '''


#ejercicio 

print("bienvenidos a la tienda")

#datos cliente
cliente_vip= True
articulos_comprados= 6
dia_semana= "lunes"

# regla 1: descuento mayorista si compra mas de 5 articulos
aplica_mayorsitas= (articulos_comprados>5) and (cliente_vip==True)

print(f"¿Aplica descuento mayorista?: {aplica_mayorsitas}")


#regla 2: de`scuento especial los lunes para clientes vip
descuento= (dia_semana=="lunes") or   ( cliente_vip==True)
print   (f"¿Aplica descuento especial?: {descuento}")


#regla 3 vereficar que la tienda no este cerrada
tienda_cerrada=False
podemos_vender= not tienda_cerrada
print(f"¿Podemos vender?: {podemos_vender}")
