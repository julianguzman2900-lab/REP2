# Arquitectura de software 

## Factory (la fabrica)
```PYTHON
#contrato
class Personaje(ABC):
    @abstractmethod
    def atacar (self):
        pass

#modelos concretos
class Guerrero(Personaje):
    def atacar(self): return "Ataca con espada"

class Mago(Personaje):
    def atacar(self): return "Ataca con magia"

# la fabrica (el corazon del patron)
class FabricaPersonaje:
    @staticmethod
    def crear_personaje(tipo):
# este metodo centraliza toda la logica de creacion 
        tipo= tipo.lower()

        if tipo = "guerrero":
            return Guerrero()
        elif tipo == "mago":

        else:
            raise ValueError(f"La fabrica no sabe crear: {tipo}")

try:
    eleccion= input("Que personaje deseas: (Guerrero / Mago)")
    #EL main no hace
    heroe= FabricaPersonajes.crear_personaje(eleccion)
    print(heroe.atacar())

except:ValueError as error:
    print(error)


# fabrica= FabricaPersonajes()
# fabrica.crear_personaje()

# #namespace
# personaje= FabricaPersonajes.crear_personaje("mago")


```

# Modelo -  Vista - Controlador

## las 3 capas
* Modelo (Model): Es el cerebro. Solo contiene datos, reglas matematicas y de validaciones.
* Vista (view): Es la cara. Solo sabe mostrar texto y capturar lo que el usuario digita. 
* Controlador (controller): El director de la orquesta. Toma los datos de la vista y los procesa en el modelo y ke devuelve el resultado a la vista para que lo imprima

```python
# MODELO ( logica pura)
class Tarea:
    def __init__(self,descripcion):
        self.descripcion= descripcion
        self.completada= False


#VISTA

class VistaTarea:
    @staticmethod
    def mostrar_menu():
        print("\n1. Agregar tarea\n2. Mostrar tarea\nSalir")
        return input("Opcion: ")

    @staticmethod
    def mostrar_list(lista):
        print("\nLista de tareas: ")


        for tarea in lista 
        print(f"{tarea.descripcion} esta en estado{tarea.completada}")

    @staticmethod
    def solicitar_descripcion():
        return input("Descripcion de la tarea: ")

#CONTROLADOR
class ControladorTareas:
    def __init__(self):
        self.tareas=[]
        self.vista= VistaTarea()

    def ejecutar(self):
        while True:
            opcion= self.vista.mostrar_menu()
            if opcion == "1":
                descripcion = self.vista.solicitar_descripcion()
                tarea= Tarea(descripcion)
                self.tareas.append(tarea)
            elif opcion == "2"
                self.vista.mostrar_lista(self.tareas)
            
            elif opcion == "3"
                self.vista.mostrar_mensaje("saliedo")

            


```

