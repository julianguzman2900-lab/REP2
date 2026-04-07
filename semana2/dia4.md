# Tareas repetitivas (for,while)
print("1")
print("2")
print("3")


## while (mientras)
El bucle `whilw` repite un bloque de codigo  *mientras* una condicion sea verdadera (`true`). En el instante en que la condicion se vuelve falsa (`False`), el ciclo termina

### sintaxis
``` python
while condicion 
    (accion respetitiva que quieeo que suceda)

    # Ejemplo 
    ```
contador= 1

print("Hola soy el ciclo while") <=3
print("contador:" contador
valor= float(input( "ingreseingrese un numero pequep de aumento))
contador=contador+ valor
```
## WHILE
```PYTHON
clave_correcta= "1234"

intento= ""

while intento != clave_correcta:

    intento= input("ingrese la clave: ")
    print("Correcta! Acceseso concedido")
```

# Ciclo `for`
`rage (cantidad)`

# forma 1: range (cantidad)
# Ejemplo
```python
#0,1,2,3,4 No con el 5
# 0,,, n-1
for index in range (5):
    print(index)
```

### forma2: range(inicio,cantidad)
```python
#1,2,3,4 No con el 5
# 1,,, n-1
for index in range (1,5):
    print(index)

```

### forma3: range(inicio, cantidad, incremento)

```python
#1,3 No con el 5
# 1,,, n-1
for index in range (1,5,2):
    print(index)
```

# ejemplo 1
```python
for numero_turno in range(5):
    print("BEEP: Producto escaneado:(turno es:)", numero_turno+1)
```

# ejemplo 2: pasillos pares
```python
for pasillo in range(0,10,2):
    print("limpiando el pasillo", pasillo+2)
```

# ejemplo 3: total del carrito de compras
```python
total=0.0

for articulo in range(4):
    precio=float(input("Ingrese el precio del articulo: "))
    total+=precio

print("El total a pagar es: ", total) 
```