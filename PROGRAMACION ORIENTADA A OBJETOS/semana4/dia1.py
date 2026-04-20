
# from abc import ABC, abstractmethod



# class Personaje(ABC):
#     @abstractmethod
#     def atacar (self):
#         pass

# #modelos concretos
# class Guerrero(Personaje):
#     def atacar(self): return "Ataca con espada"

# class Mago(Personaje):
#     def atacar(self): return "Ataca con magia"

# # la fabrica (el corazon del patron)
# class FabricaPersonaje:
#     @staticmethod
#     def crear_personaje(tipo):
# # este metodo centraliza toda la logica de creacion 
#         tipo= tipo.lower()

#         if tipo == "guerrero":
#                     return Guerrero()
#         elif tipo == "mago":
#              return Mago()
#         else:
                    
#             raise ValueError(f"La fabrica no sabe crear: {tipo}")

# try:
#     eleccion= input("Que personaje deseas: (Guerrero / Mago)")
#     #EL main no hace
#     heroe= FabricaPersonaje.crear_personaje(eleccion)
#     print(heroe.atacar())

# except ValueError as error:
#     print(error)



# # MODELO ( logica pura)
# class Tarea:
#     def __init__(self,descripcion):
#         self.descripcion= descripcion
#         self.completada= False


# #VISTA

# class Tarea:
#     def __init__(self, descripcion):
#         self.descripcion = descripcion 
#         self. completada = False


# # VISTA 
# class VistaTarea:
#     @staticmethod
#     def mostrar_menu():
#         print("\n 1. Agregar tarea\n 2. Mostar tarea\n 3. Salir")
#         return input("Opción: ")

#     @staticmethod
#     def mostrar_lista(lista):
#         print("\nLista de tareas: ")

#         for tarea in lista:
#             estado = "Completada" if tarea.completada else "Pendiente"
#             print(f"{tarea.descripcion} está en estado: {estado}")

#     @staticmethod
#     def solicitar_descripcion():
#         return input("Descripción de la tarea: ")
    
#     def mostrar_mensaje(self,mensaje):
#         print(mensaje)

# # CONTROLADOR
# class ControladorTareas:
#     def __init__(self):
#         self.tareas = []
#         self.vista = VistaTarea()

#     def ejecutar(self):
#         while True:
#             opcion = self.vista.mostrar_menu()
#             if opcion == "1":
#                 descripcion = self.vista.solicitar_descripcion()
#                 tarea = Tarea(descripcion)
#                 self.tareas.append(tarea)
#             elif opcion == "2":
#                 self.vista.mostrar_lista(self.tareas)
#             elif opcion == "3":
#                 self.vista.mostrar_mensaje("Saliendo...")
#                 break
    

# # inicio del programa 
# if __name__ == "__main__":
#     controlador = ControladorTareas()
#     controlador.ejecutar()
                


class LibroBiblioteca:
    def __init__(self,titulo,autor,id):
        self.titulo= titulo
        self.autor= autor
        self.id= id
        self.prestado= True

class VistaBiblioteca:
    @staticmethod
    def mostar_menu():
        print()

