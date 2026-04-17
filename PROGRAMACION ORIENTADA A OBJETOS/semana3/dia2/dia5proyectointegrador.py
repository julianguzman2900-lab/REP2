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

    def atender_paciente(self):
         self.realizar_trabajo()

         nota= input("Ingrese la nota")
         paciente.historial.agregar_observacion(nota)



class Enfermero(PersonalMedico):
    def realizar_trabajo(self):
            print(f"[SISTEMA] El enfermero {self.nombre} esta aplicando cuidados y revisando signos vitales")



class HistorialClinico:
    def __init__(self):
         self.observaciones= []
    def agregar_observacion(self,texto):
         self.observaciones.append(texto)



class paciente:
     def __init__(self,nombre,edad):
          self.nombre= nombre
          self.edad = edad 
          self.salud = 100
          self.historial= HistorialClinico()

     
     def estado(self):
        if self.salud < 20:
            return "CRITICO"
        else:
            return "ESTABLE"