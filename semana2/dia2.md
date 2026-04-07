# Repaso
* tipos de datos
* operadores aritmeticos
* tipos de operaciones especiales modulo, division entera
* operadores logicos (and, not,or)
* operadores operativos (>, >, == >=, <=, !=)
* casting: int(), float(), str()



# Condicionales
## La regla basica: el `if`

bloque condicional del if  
    me indica que esto le pertenece al bloque
    esto tambien le pertenece



### SINTAXIS:
```python
if condicion
accion 
```


### ejemplo
```python 
Dinero = 1000
precio = 750
if dinero>= precio:
    print("venta aprobada)
```


### Practica guiada
* programa de sistema para ingresar a la bodega
```python
print ("=== SISTEMA DE SEGURIDAD DE LA BODEGA===")

clave_ingresada= input(" imgrewse la,clae de deguridad:")

clave_correcta= "1234"

if clave_ingresada == clave_correcta:
    print("Clave correcta. Acceso permitido.")
    print("Bienvenido a la bodega super segura")

    
print("Fin del programa.")
```



## Condicional `else`

* nunca lleva una condicion al lado
* es el nasurero que recoge cualquier cosa que no haya cumplido con la condicion 
```python
dinero= float(input("dinero del cliente:"))
precio= 1200

if dinero >= precio:
    print("puede comprar el producto")
else:
    print("no puede comprar el producto")
```



### Ejercicio estudiantes

```
un cine desea automatizar una parte de su sistema de control de acceso.
El sistema debe de verificar si una persona puede ingresar a una pelicula para mayores de edad 

el programa debe solicitar al usuario 
- edad de la persona
- si posee entrada comprada (responder un si o no)
si la persona tiene 18+ y tiene entrada puede ingresar a la pelicula de lo contrario, no se le permite la entrada
```
```python
print("=== SISTEMA DE CONTROL DE CINE CHAPIN ===")
print("Bienvenido a cine Chapin")
pelicula = input("Ingrese el nombre de la pelicula que vera: ")
edad = int(input("Ingrese su edad: "))
entrada= input("Usted cuenta con entrada para la pelicula? (si/no): ")
if (edad >=18) and ( entrada =="si")    :
    print("----------------------------------------------------------")
    print(f"Usted si puede ingresar a la pelicula {pelicula}")
    print("----------------------------------------------------------")
else:
    print("----------------------------------------------------------")
    print(f"Usted no puede ingresar a la pelicula {pelicula}")   
    print("----------------------------------------------------------")
print("=== GRACIAS POR USAR NUESTRO SISTEMA CINE CHAPIN ===") 
```


## condicional `elif`

```python
edad= int(input("Digite su dato"))
precio_entrada= 200

if edad <= 12:
    print(" El cliente es un nino, tiene un descuenti del 50%")
    total= precio_entrada * 0.5
elif edad >= 60:
    print(" El cliente es un adulto mayor, tiene un descuento del 25%")
    total= precio_entrada * 0.75
else:
    print(" El cliente es un adulto, no tiene descuento")
    total= precio_entrada

print(" El total a pagar es: ", total)
```

### Ejercicio estudiantes

```python
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
    
```


#### Condicional: SWITCH

