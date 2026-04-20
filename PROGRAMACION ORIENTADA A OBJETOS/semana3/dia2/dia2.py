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
#         contador = 0
#         for paciente in self.pacientes:
#          print(contador, paciente.nombre, paciente.edad, paciente.salud, paciente.estado())
#         contador = contador + 1


#     def mostrar_personal(self):
#      contador = 0
#      for persona in self.personal:
#         print(contador, persona.nombre, persona.especialidad)
#         contador = contador + 1
#     def consulta(self):
#         if len(self.personal) == 0 or len(self.pacientes) == 0:
#             print("No hay datos")
#             return

#         self.mostrar_personal()
#         medico = int(input("Elija medico: "))
#         medico = self.personal[medico]

#         self.mostrar_pacientes()
#         paciente = int(input("Elija paciente: "))
#         paciente = self.pacientes[paciente]

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





from abc import ABC, abstractmethod

# --- BLOQUE 1: Personal Médico ---
class PersonalMedico(ABC):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    @abstractmethod
    def realizar_labor(self):
        pass

class Doctor(PersonalMedico):
    def realizar_labor(self):
        print(f"[SISTEMA] El Dr. {self.nombre} está realizando un diagnóstico especializado.")

    def atender_paciente(self, paciente):
        self.realizar_labor()
        nota = input("Ingrese nota para el historial: ")
        paciente.historial.agregar_observacion(nota)
        
        while True:
            try:
                dosis = int(input("Ingrese dosis de recuperación (1-50): "))
                paciente.salud += dosis
                if paciente.salud > 100:
                    paciente.salud = 100
                print(f"¡Tratamiento Exitoso! La salud de {paciente.nombre} ha subido a {paciente.salud}%.")
                break
            except ValueError:
                print("[ERROR]: Solo se permiten valores numéricos para la dosis. Intente de nuevo.")

class Enfermero(PersonalMedico):
    def realizar_labor(self):
        print(f"[SISTEMA] El enfermero/a {self.nombre} está aplicando cuidados y revisando signos vitales.")

# --- BLOQUE 2: Historial y Paciente ---
class HistorialClinico:
    def __init__(self):
        self.observaciones = []

    def agregar_observacion(self, texto):
        self.observaciones.append(texto)

    def mostrar_notas(self):
        print(f"--- Historial Clínico ---")
        for nota in self.observaciones:
            print(f"- {nota}")

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.salud = 15 # Salud inicial para prueba
        self.historial = HistorialClinico()

    def estado(self):
        if self.salud < 20:
            return "[CRÍTICO]"
        return "[ESTABLE]"

# --- BLOQUE 4: El Sistema Hospitalario ---
class Hospital:
    def __init__(self):
        self.pacientes = []
        self.personal = []

    def registrar_paciente(self):
        nombre = input("Nombre del paciente: ")
        while True:
            try:
                edad = int(input("Edad: "))
                break
            except ValueError:
                print("[ERROR] Ingrese un número válido.")
        nuevo_p = Paciente(nombre, edad)
        self.pacientes.append(nuevo_p)
        print("[SISTEMA] Paciente registrado]")

    def contratar_personal(self):
        nombre = input("Nombre del médico: ")
        especialidad = input("Especialidad (o 'Cuidados' para enfermero): ")
        if especialidad.lower() == "cuidados":
            self.personal.append(Enfermero(nombre, especialidad))
        else:
            self.personal.append(Doctor(nombre, especialidad))

    def mostrar_pacientes(self):
        print("\n-- Pacientes en Espera --")
        contador = 0
        for paciente in self.pacientes:
            print(f"{contador}. {paciente.nombre} (Edad: {paciente.edad} | Salud: {paciente.salud}% {paciente.estado()})")
            contador = contador + 1

    def mostrar_personal(self):
        print("\n-- Personal Disponible --")
        contador = 0
        for personal in self.personal:
            print(f"{contador}. {personal.nombre} ({personal.especialidad})")
            contador = contador + 1

# --- Lógica del Menú ---
hospital = Hospital()
while True:
    print("\n>>> SISTEMA HOSPITALARIO VIDA-SANA <<<")
    print("1. Registrar Paciente\n2. Contratar Personal\n3. Realizar Consulta Médica\n4. Ver Reporte de Pabellón\n5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        hospital.registrar_paciente()
    elif opcion == "2":
        hospital.contratar_personal()
    elif opcion == "3":
        hospital.mostrar_personal()
        try:
            eleccion_doctor = int(input("Elija el médico: "))
            hospital.mostrar_pacientes()
            eleccion_paciente = int(input("Elija el paciente: "))
            
            medico = hospital.personal[eleccion_doctor]
            paciente = hospital.pacientes[eleccion_paciente]
            
            if isinstance(medico, Doctor):
                medico.atender_paciente(paciente)
            else:
                medico.realizar_labor()
        except (ValueError, IndexError):
            print("[ERROR] Selección no válida.")
    elif opcion == "4":
        hospital.mostrar_pacientes()
    elif opcion == "5":
        break
