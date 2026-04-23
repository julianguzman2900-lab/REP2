
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
                




# class VistaBiblioteca:
#     @staticmethod
#     def mostar_menu():
#       pass

# MODELO
class Libro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.prestado = False

    def prestar(self):
        self.prestado = True


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
  

    def listar_libros(self):
        return self.libros

    def prestar_libro(self, id):
        for libro in self.libros:
            if libro.id == id:
                libro.prestar()
               

# VISTA
class VistaBiblioteca:
    def menu(self):
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Prestar libro")
        print("4. Salir")
        return input("Opción: ")

    def mostrar_libros(self, libros):
        for libro in libros: 
            situacion = "Prestado" if libro.prestado else "Disponible" 
            print("LIBRO |  AUTOR  | ID | ESTADO")
            print(f"{ libro.titulo}  | { libro.autor} |  {libro.id} {situacion} ")
     



# CONTROLADOR
class ControladorBiblioteca:
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.vista = VistaBiblioteca()

    def iniciar(self):
        while True:
            opcion = self.vista.menu()

            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                id = input("ID: ")
                libro = Libro(titulo, autor, id)
                self.biblioteca.agregar_libro(libro)
                print("Libro agregado exitosamente")

            elif opcion == "2":
                libros = self.biblioteca.listar_libros()
                self.vista.mostrar_libros(libros)

            elif opcion == "3":
                id = input("ID del libro: ")
                self.biblioteca.prestar_libro(id)
                print("El libro fue prestado ")


            elif opcion == "4":
                print("Saliendo...")
                break


# EJECUCIÓN
libro1 = ControladorBiblioteca()
libro1.iniciar()