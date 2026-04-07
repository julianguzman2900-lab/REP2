#==================================
# Ejercicio 1
#==================================

# solucion ejercicio 1
print("Torneo juvenil")
print("Bienvenido al torneo juvenil de fútbol. Para participar, debes cumplir con los siguientes requisitos:")
nombre_participante = input("Ingrese el nombre del participante: ")
edad = int(input("Ingrese la edad del participante: "))
inscripcion = input("¿El participante cuenta con inscripción en el torneo? (si/no): ")

if edad >=15 and inscripcion== "si":
    print(f"{nombre_participante} fue autorizado para ingresar al torneo.")
else:
    print(f"{nombre_participante} no fue autorizado para ingresar al torneo.")



#==================================
# Ejercicio 2
#==================================

# solucion ejercicio 2

bateria = int(input("Ingrese el porcentaje de batería: "))
if bateria<=20:
    print("Debe cargar el celular")

else:
    print("La batería es suficiente")



#==================================
# Ejercicio 3   
#==================================

# solucion ejercicio 3

print("Clasificacion de paquetes")
peso = float(input("Ingrese el peso del paquete en kg: "))
if peso < 1:
    print("Paquete ligero")       
elif peso >= 1 and peso <=5:
    print("Paquete estandar")
elif peso > 5:
    print("Paquete pesado")


#==================================
# Ejercicio 4   
#==================================

# solucion ejercicio 4

color = input("Ingrese el color del semáforo: ")
if color == "verde":
    print("Avanzar")
elif color == "amarillo":
    print("Precaución")
else:
    print("Detenerse")


#==================================
# Ejercicio 5
#==================================

# solucion ejercicio 5

print("Sistema de autorizacion para area VIP")
nombre_cliente = input("Ingrese el nombre del cliente: ")
edad = int(input("Ingrese la edad del cliente: "))
entrada= input("Ingrese su tipo de entrada, VIP o General: ")


if edad >= 18 and entrada == "VIP": 
    print(f"{nombre_cliente} fue autorizado para ingresar al area VIP.")
    bebida = input("¿Desea una bebida especial? (si/no): ")
    if bebida == "si":
        dinero_disponible = float(input("Ingrese el dinero disponible para la bebida: "))
        precio_bebida= float(input("Ingrese el precio de la bebida: "))
        cambio = dinero_disponible - precio_bebida
        if dinero_disponible >= precio_bebida:
            print("La bebida ha sigo aprobada")
            print(f"Su cambio es: {cambio}")
        else:
            
            print("La bebida no fue aprobada")
    else:
        print("Disfrute de su acceso VIP")

else:
    print(f"{nombre_cliente} no fue autorizado para ingresar al area VIP.")


#==================================
# Ejercicio 6
#==================================

# solucion ejercicio 6

print("Sistema de asignacion de beca estudiantil")
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
promedio_final= float(input("Ingrese el promedio final del estudiante: "))
ingreso_famiiliar = float(input("Digite el ingreso familiar mensual : "))
materias_aprobadas = int(input("Ingrese la cantidad de materias aprobadas: "))

if promedio_final < 70 :
    print("El estudiante no es elegible para la beca")
elif promedio_final <= 84 and ingreso_famiiliar <= 4000:
    print("El estudiante es elegible para una beca parcial")
    print("El monto asignado es de Q.2250.00")
elif promedio_final >= 85 and ingreso_famiiliar <=4000 and materias_aprobadas > 5:
    print("El estudiante es elegible para una beca completa")
    print("El monto asignado es de Q.4500.00")
else:
    print("El estudiante no es elegible para la beca")


#==================================
# Ejercicio 7   
#==================================

# solucion ejercicio 7


