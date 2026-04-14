# class Producto:
    # def __init__(self,nombre,precio):
    #     self.nombre = nombre
    #     self.precio = precio
        
    # def __add__(self,otro_producto):
    #     suma_productos= self.precio + otro_producto.precio
    #     return Producto(suma_productos)
    
    # def __sub__(self,otro_producto):
    #     resta_productos= self.precio - otro_producto.precio
    #     return Producto(resta_productos)
    # def __eq__(self, otro_producto):
    #     comparacion_productos= self.precio == otro_producto.precio
    #     return comparacion_productos



#EJERCICIO 


# 1.
import random
numeros= random.randint(1,10)

print(f"El numero seleccionado es: {numeros}")

#2.
from random import choice
lista= ["Ana", "Luis", "Carlos"]

nombre= choice(lista)
print(f"El nombre seleccionado es: {nombre}")


import math as matematicas
numero = matematicas.ceil(4.2)
print(f"El número redondeado es: {numero}")
