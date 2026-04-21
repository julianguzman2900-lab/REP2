# class Bateria:
#     def __init__(self):
#         self.porcentaje = 100

#     def descargar(self):
#         self.porcentaje -= 10
#         print(f"Batería al {self.porcentaje}%")


# class Celular:
#     def __init__(self, marca):
#         self.marca = marca
#         self.energia = Bateria()

#     def usar_app(self):
#         print("Abriendo aplicación...")
#         self.energia.descargar()


# celular1 = Celular("Samsung")
# celular1.usar_app()
# celular1.usar_app()



# class Arma:
#     def __init__(self, nombre, puntos_dano):
#         self.nombre = nombre
#         self.puntos_dano = puntos_dano


# class Guerrero:
#     def __init__(self, nombre, arma_equipada):
#         self.nombre = nombre
#         self.arma = arma_equipada

#     def atacar(self):
#         print(f"{self.nombre} ataca con {self.arma.nombre} causando {self.arma.puntos_dano} de daño")


# arma = Arma("Espada Larga", 50)
# guerrero = Guerrero("Jochu", arma)

# guerrero.atacar()


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} escrito por {self.autor}"


class Biblioteca:
    def __init__(self, nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal
        self.catalogo = []

    def agregar_libro(self, nuevo_libro):
        self.catalogo.append(nuevo_libro)

    def mostrar_inventario(self):
        print(f"Inventario de {self.nombre_sucursal}:")
        for libro in self.catalogo:
            print(libro)


libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("El principito", "Antoine de Saint-Exupéry")

biblioteca1 = Biblioteca("Biblioteca Municipal")

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)

biblioteca1.mostrar_inventario()