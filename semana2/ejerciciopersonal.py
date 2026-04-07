# print("Ingreso de cargamento de latas de atun")

# cantidad_latas = int(input("ingrese la cantidad de latas:"))


# print("\n===**RESULTADOS**=====")
# espacio_stanteria= 10
# resultado=int(cantidad_latas/espacio_stanteria)
# print("la cantidad de estantes llenos es de:", resultado)

# resto= cantidad_latas%espacio_stanteria
# print("la cantidad de latas sobrantes par exhibicion es de:", resto)




print("Bienvenido a la academia")

print("ingrese su edad")
edad = int(input("Edad: "))
print("usted cuenta con membresia para nuentra academia?")
membresia = input("Membresia (si/no): ")
puede_ingresar= (edad >=18) and ( membresia =="si")
print("\n===**RESULTADOS**=====")
print(f"¿Puede ingresar a la academia?: {puede_ingresar}")