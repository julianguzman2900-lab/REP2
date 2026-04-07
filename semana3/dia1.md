# Funciones o metodos
## sintaxis:
para crear una funcion, vamos a usar la palabra reservada `def` (viene de **define** en ingles).Le asignamos un nombre.Abrimos y cerramos parentesis`()`, y luego terminamos con`:`

ocupamos la identacion para indicar que le pertenece a la funcion


```python 
def saludo ():
    print("hola como estas?")

#EJEMPLO EJERCICIO
    def saludo ():
    print("hola como estas?")
def despedida():    
        print("adios, hasta luego")


def menu():
    print("1. Saludo")
    print("2. Despedida")
    print("3. Salir")

    opcion= input("Ingrese una opcion: ")

    while True:
        match opcion:
            case "1":
                saludo()
            case "2":
                despedida()
            case "3":
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")
        opcion = input("Ingrese una opcion: ")


saludo()
despedida()
menu()
```
