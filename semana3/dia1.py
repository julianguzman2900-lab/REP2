def saludo():
    print("hola como estas, ?")
def despedida():    
        print("adios, hasta luego ")


def menu():
    print("1. Saludo")
    print("2. Despedida")
    print("3. Salir")

    
    nombre = input("Ingrese un nombre: ")
    opcion= input("Ingrese una opcion: ")


    while True:
        match opcion:
            case "1":
                saludo(nombre)
            case "2":
                despedida(nombre)
            case "3":
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")
        opcion = input("Ingrese una opcion: ")


saludo()
despedida()
menu()