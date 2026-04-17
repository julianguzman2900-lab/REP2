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


# # 1.
# import random
# numeros= random.randint(1,10)

# print(f"El numero seleccionado es: {numeros}")

# #2.
# from random import choice
# lista= ["Ana", "Luis", "Carlos"]

# nombre= choice(lista)
# print(f"El nombre seleccionado es: {nombre}")


# import math as matematicas
# numero = matematicas.ceil(4.2)
# print(f"El número redondeado es: {numero}")












# from abc import ABC, abstractmethod

# # -------- BLOQUE 1 --------
# class PersonalMedico(ABC):
#     def __init__(self, nombre, especialidad):
#         self.nombre = nombre
#         self.especialidad = especialidad

#     @abstractmethod
#     def realizar_labor(self):
#         pass


# class Doctor(PersonalMedico):
#     def realizar_labor(self):
#         print(f"{self.nombre} está haciendo un diagnóstico")

#     def atender_paciente(self, paciente):
#         self.realizar_labor()

#         nota = input("Ingrese nota: ")
#         paciente.historial.agregar_observacion(nota)

#         while True:
#             try:
#                 dosis = int(input("Ingrese dosis: "))
#                 paciente.salud += dosis

#                 if paciente.salud > 100:
#                     paciente.salud = 100

#                 print(f"Salud actual: {paciente.salud}%")
#                 break
#             except:
#                 print("Error, ingrese un número")


# class Enfermero(PersonalMedico):
#     def realizar_labor(self):
#         print(f"{self.nombre} está revisando signos vitales")


# # -------- BLOQUE 2 --------
# class HistorialClinico:
#     def __init__(self):
#         self.observaciones = []

#     def agregar_observacion(self, texto):
#         self.observaciones.append(texto)


# class Paciente:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#         self.salud = 100
#         self.historial = HistorialClinico()

#     def estado(self):
#         if self.salud < 20:
#             return "CRITICO"
#         else:
#             return "ESTABLE"


# # -------- BLOQUE 4 --------
# class Hospital:
#     def __init__(self):
#         self.pacientes = []
#         self.personal = []

#     def registrar_paciente(self):
#         nombre = input("Nombre: ")
#         edad = int(input("Edad: "))
#         self.pacientes.append(Paciente(nombre, edad))

#     def contratar_personal(self):
#         nombre = input("Nombre: ")
#         tipo = input("1 Doctor / 2 Enfermero: ")

#         if tipo == "1":
#             self.personal.append(Doctor(nombre, "Doctor"))
#         else:
#             self.personal.append(Enfermero(nombre, "Enfermero"))

#     def mostrar_pacientes(self):
#         for i, p in enumerate(self.pacientes):
#             print(i, p.nombre, p.edad, p.salud, p.estado())

#     def mostrar_personal(self):
#         for i, p in enumerate(self.personal):
#             print(i, p.nombre, p.especialidad)

#     def consulta(self):
#         if len(self.personal) == 0 or len(self.pacientes) == 0:
#             print("No hay datos")
#             return

#         self.mostrar_personal()
#         i = int(input("Elija medico: "))
#         medico = self.personal[i]

#         self.mostrar_pacientes()
#         j = int(input("Elija paciente: "))
#         paciente = self.pacientes[j]

#         if isinstance(medico, Doctor):
#             medico.atender_paciente(paciente)
#         else:
#             medico.realizar_labor()

#     def reporte(self):
#         self.mostrar_pacientes()


# # -------- MENU --------
# hospital = Hospital()

# while True:
#     print("\n1. Registrar Paciente")
#     print("2. Contratar Personal")
#     print("3. Consulta")
#     print("4. Reporte")
#     print("5. Salir")

#     op = input("Opcion: ")

#     if op == "1":
#         hospital.registrar_paciente()
#     elif op == "2":
#         hospital.contratar_personal()
#     elif op == "3":
#         hospital.consulta()
#     elif op == "4":
#         hospital.reporte()
#     elif op == "5":
#         break
#     else:
#         print("Opcion invalida")