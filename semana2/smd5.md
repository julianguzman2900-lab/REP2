# Uso del brake
```python
while True:
    nombre= input("ingrese su nombre... (salir para terminar):")
    
    if nombre =="salir":
        break

    print("Bienvenido:", nombre)

print("Programa finalizado")
```
# continue
```python
for producto in range(6):
    if producto== 3:
        continue
    print("producto etiquetado:", producto)
```

# Estructura  de datos
## Forma 1: con elementos crear una Lista 

mi_lista= [10, "hola",3.14,]

## forma 2: sin elementos

lista_vacia=[]


## Acceder a los elementos
saludo=mi_lista [1]
print(saludo)


### un paso
print(mi_lista[1])

### indices negativos
print(mi_lista[-1])

### por porcion de la lista(slicing)

`nombre de la lista`+`[`+inicio`:`+`final`+`]`
mi_lista[1:3]

in range(1,5) [1,2,3,4]

## slicing con saltos 

`nombre de la lista`+`[`+inicio`:`+`final`+`:`+`paso/incremento`+`]`

mi_lista[0:4:2]


#  Agregar elementos (append)

### sintaxis
`nombre de la lista` +`.`+`append`(+ `lo que quiero agregar`+`)` lista_vacia.append("julian")

print(lista_vacia[0])

mi_lista.append("mundo")

print(mi_lista)

# Recorrer una lista
## forma 1 ciclo for
```python
for elemento in mi_lista:
    print(elemento)

    if elemento== 3.14:
        print("encontre el numeor pi")
        break
```
# forma 2 usando los indices
# len(mi_mi lista) devuelve la cantidad de elementos que tiene la lista

```python
for indice in range(len(mi_lista)):
    print(mi_lista[indice])

```

# Modificar un elemento
mi_lista= "HOLA'


# Eliminar un elemento por valor

mi_lista.remove(10)


# ELIMINAR VALOR DE MI INDICE `del`
del mi_lista[1]




# Eliminar el ultimo elemnto `pop`

mi_lista.pop()



# Estructura de tuplas 

