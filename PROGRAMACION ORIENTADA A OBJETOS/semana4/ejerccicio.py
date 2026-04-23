from abc import ABC, abstractmethod

class EnergiaInvalidaError(Exception):
    pass

class Nucleo:
    def __init__(self, id):
        self.id = id

class EntidadBase(ABC):
    def __init__(self, energia, id):
        if energia < 0:
            raise EnergiaInvalidaError("Energía no puede ser negativa")
        self.energia = energia
        self.nucleo = Nucleo(id)

    @abstractmethod
    def alimentarse(self, cantidad=10):
        pass

    def __add__(self, otra_energia):
        return self.energia + otra_energia.energia


class Sintetizador(EntidadBase):
    def alimentarse(self, cantidad=10):
        self.energia += cantidad


class Consumidor(EntidadBase):
    def alimentarse(self, cantidad=10):
        self.energia += cantidad


class Hibrido(Sintetizador, Consumidor):
    def __init__(self, energia, id):
        super().__init__(energia, id)
        self.nucleo = Nucleo(id)

    def alimentarse(self, cantidad=10):
        self.energia += cantidad * 2
        print("Híbrido ganó", cantidad * 2, "de energía")


def iniciar_ciclo_vital(lista_entidades):
    for entidad in lista_entidades:
        entidad.alimentarse()


lista_entidades = []
id_actual = 1

while True:
    print("\n¿Qué tipo de entidad desea crear?")
    print("1. Sintetizador")
    print("2. Consumidor")
    print("3. Híbrido")
    opcion = input("Elija una opción (1-3): ")

    if opcion == "1" or opcion == "2" or opcion == "3":
        try:
            energia = int(input("Energía inicial: "))
            if energia < 0:
                raise EnergiaInvalidaError("La energía no puede ser negativa")

            if opcion == "1":
                entidad = Sintetizador(energia, id_actual)
            elif opcion == "2":
                entidad = Consumidor(energia, id_actual)
            elif opcion == "3":
                entidad = Hibrido(energia, id_actual)

            lista_entidades.append(entidad)
            id_actual += 1

        except ValueError as error:
            print("Error:", error)
        except EnergiaInvalidaError as error:
            print("Error:", error)

    else: 
        print("Opción no válida, intente de nuevo")


    print("\n=== INICIANDO CICLO VITAL ===")
    iniciar_ciclo_vital(lista_entidades)

    if lista_entidades:
        total = 0
        for entidad in lista_entidades:
            total += entidad.energia
        print("Energía total:", total)
    else:
        print("No hay entidades")