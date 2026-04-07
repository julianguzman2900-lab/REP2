# Estructura de datos 
## diccionarios 
Se usa lo que se llama clave-valor

Le ponems una etiqueta con nombre (Clave) a la caja  y adentro guardamos la información (Valor)

clave: valor 


**Sintaxis** A diferencia de las listas que usan corchete `[]`  los diccionarios se crean usando llaves `{}`

```python

producto = {
    "nombre": "arroz",
    "precio": 1200.0,
    "cantidad": 5
}

print(producto["nombre"])
print(producto["precio"])


total = producto["precio"] * producto["cantidad"]
print("El total a pagar es:", total)
}
print(producto)
```




Un diccionario es ideal  cuado queremos que cada dato tenga una atiqueta que lo identifique, es decir, una clave.


## modificar los valores de un diccionario
<!--en una lista-->
lista_edades[5]=50
<!--en un diccionario-->
producto["precio"]=1500.0

# Ejercicio
```python
clientes= {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print(clientes)

clientes["ciudad"] = "Barcelona"

clientes["edad"] = clientes["edad"] + 1
print(clientes)
```

## Agregar nuevos elementos a un diccionario

```python
roducto = {
    "nombre": "arroz",
    "precio": 1200.0,
    "cantidad": 5
}

print(producto["nombre"])
print(producto["precio"])


producto["categoria"] = "granos"
print(producto)
```


# Recorrer un diccionario

## forma 1 solo las claves

```python

for clave in producto:
    print(f"clave: {clave} valor:{producto})
```

## forma 2 usando el método items()

```python

for clave, valor in producto.items():
    print(f"clave:{clave}; valor {valor}")
    ```
    