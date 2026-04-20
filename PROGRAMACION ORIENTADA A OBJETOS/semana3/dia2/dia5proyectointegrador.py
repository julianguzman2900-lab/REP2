from abc import ABC,abstractmethod
class PersonalMedico (ABC):
    def __init__(self,nombre,especialidad):
        self.nombre = nombre
        self.especialidad = especialidad


    @abstractmethod
    def realizar_trabajo(self):
        pass 

class Doctor(PersonalMedico):
    def realizar_trabajo(self):
            print(f"[SISTEMA] El Dr. {self.nombre} esta realizando un diagnostico especial")

    def atender_paciente(self, paciente):
        self.realizar_labor()

        nota = input("Ingrese nota: ")
        paciente.historial.agregar_observacion(nota)

        while True:
            try:
                dosis = int(input("Ingrese dosis: "))
                paciente.salud += dosis

                if paciente.salud > 100:
                    paciente.salud = 100

                print(f"Salud actual: {paciente.salud}%")
                break
            except:
                print("Error, ingrese un número")



class Enfermero(PersonalMedico):
    def realizar_trabajo(self):
            print(f"[SISTEMA] El enfermero {self.nombre} esta aplicando cuidados y revisando signos vitales")



class HistorialClinico:
    def __init__(self):
         self.observaciones= []

    def agregar_observacion(self,texto):
         self.observaciones.append(texto)

    def mostrar_notas(self):
            print(f"--- Historial Clínico ---")
            for nota in self.observaciones:
                print(f"- {nota}")

class Paciente:
     def __init__(self,nombre,edad):
          self.nombre= nombre
          self.edad = edad 
          self.salud = 30
          self.historial= HistorialClinico()

     
     def estado(self):
        if self.salud < 20:
            return "CRITICO"
        else:
            return "ESTABLE"

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
        print("[SISTEMA] Nuevo paciente registrado]")
  
    def contratar_personal(self):
         nombre= input("Ingrese su nombre: ")
         puesto= int(input("Ingrese el puesto contratado | 1.Doctor | 2.Enfermero: "))

         if puesto== 1:
             self.personal.append(Doctor(nombre,"Doctor"))
            
            
         else:
            self.personal.append(Enfermero(nombre, "Enfermero"))
            print("[SISTEMA] Nuevo personal registrado")
     
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
        except (ValueError):
            print("[ERROR] Selección no válida.")
    elif opcion == "4":
        hospital.mostrar_pacientes()
    elif opcion == "5":
        break
