# Concepto abstracto
## Creando el molde fantasma (el módulo `abc`)

# abc -> Abstract Base Classes
# debemos marcar al menos uno de sus métodos con el decorador @abstractmethod.
# un método abstracto es un método vacío. No tiene código por dentro. usamos la palabra pass

```python
# importacion OBLIGATORIA
from abc import ABC, abstractmethod

class Documento(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

    @abstractmethod
    def exportar(self):
        pass

    def mostrar_titulo(self):  # opcional: los padres abstractos pueden tener métodos normales
        print(f"Documento: {self.titulo}")

try:
    doc_invalido = Documento("Mi archivo")
except:
    print("[BLOQUE]")

```

**El HIJO esta obligado a sobreescribir los metodos del padre**




## PROPIEDADES ABSTRACTAS
Ponemos `@property` seguido de `@abstractmethod`
*"Estas obligado a crear Getter para esta propiedad*,

```python
from abc import ABC,abstractmethod
class VehiculoComercial(ABC):
    @property
    @abstractmethod
    def tarifa_km(self):
        pass

def calcular_viaje(self,kilometro):
    total= kilometro*self.tarifa_km
    print(f"Costo del viaje{total}")

class Taxi(VehiculoComercial)
    @property
    def tarifa_km(self):
        return 500

mi_taxi=Taxi()
mi_taxi.calcular_viaje(10)
```
# HERENCIA MULTIPLE


