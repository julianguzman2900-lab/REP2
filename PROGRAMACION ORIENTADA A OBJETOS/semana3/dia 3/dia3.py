# class SableDeLuz:
#     def __init__(self, energia=0):
#         self.energia = energia

#     def recarga(self, nueva_energia=10):
#         self.energia += nueva_energia

#     def __sub__(self, otro_objeto):
#         return SableDeLuz(self.energia - otro_objeto.energia)


# # Crear objetos
# sable1 = SableDeLuz(50)
# sable2 = SableDeLuz(20)

# # Restar
# sable3 = sable1 - sable2

# # Mostrar resultado
# print(f"Energia sable1: {sable1.energia}")
# print(f"Energia sable2: {sable2.energia}")


## EJERCICIO


# 

# from abc import ABC,abstractmethod
# class VehiculoComercial(ABC):
#     @property
#     @abstractmethod
#     def tarifa_km(self):
#         pass

#     def calcular_viaje(self, kilometro):
#         total = kilometro * self.tarifa_km
#         print(f"Costo del viaje: {total}")

# class Taxi(VehiculoComercial):
#     @property
#     def tarifa_km(self):
#         return 500

# mi_taxi=Taxi()
# mi_taxi.calcular_viaje(10)


from abc import ABC, abstractmethod

class VehicculoTerrestre(ABC):
    @property
    @abstractmethod
    def conducir_ruedadas(self):
        pass
    
class VehiculoAcuatico(ABC):
    @property
    @abstractmethod
    def encender_helices(self):
        pass


class VehicuoAnfibio(VehicculoTerrestre, VehiculoAcuatico):
    @property
    def conducir_ruedadas(self):
        return "Activando traccion 4x4 en terreno rocoso"

    @property
    def encender_helices(self):
        return "Retrayendo ruedas y activando propulsor acuatico"
    

class AutoComun(VehicculoTerrestre):
    @property
    def conducir_ruedadas(self):
        return "Conduciendo en carretera asfaltada"

class Lancha(VehiculoAcuatico):
    @property
    def encender_helices(self):
        return "Activando propulsor acuatico"
    
auto=AutoComun()
lancha=Lancha()
anfibio=VehicuoAnfibio()

ruta_terrestre= [auto,anfibio]
for vehiculo in ruta_terrestre:
    print(vehiculo.conducir_ruedadas)

ruta_acuatica= [lancha,anfibio]
for vehiculo in ruta_acuatica:
    print(vehiculo.encender_helices)