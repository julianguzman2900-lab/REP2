# class vehiculo:
#     def encender_motor(self):
#         print("[SITEMA] | EL MOTOR SE HA ENCENDIDO.")

#     def apagar_motor(self):
#         print("[SITEMA] | EL MOTOR SE HA APAGADO.")

# #subclase 1(hijo)
# class Auto(vehiculo):
#     def encender_aire(self):
#         print("[AUTO] | Aire acondicionado esata encendido.")

# class Moto(vehiculo):
#     def hacer_acrobacia(self):
#         print("[MOTO] | Levantando la rueda delantera.")
    
# carro= Auto()
# moto=   Moto()


# print("Acciones del auto")
# carro.encender_motor()
# carro.encender_aire()

# print("\nAcciones de la moto")
# moto.encender_motor()
# moto.hacer_acrobacia()


# class PersonajeBase:
#     def caminar(self):
#         print("El personaje esta avanzando por el mapa.")
    
#     def descansar(self):
#         print("El personaje esta recuperando energia.")


# class Mago(PersonajeBase):
#     def lanzar_hechizo(self):
#         print("El mago lanza una bola de fuego.")

# class Guerrero(PersonajeBase):
#     def bloquear_ataque(Self):
#         print("El guerrero levanta su escudo de metal")


# mi_mago= Mago()
# mi_guerrero= Guerrero()

# print("\nAcciones del mago")
# mi_mago.caminar()
# mi_mago.descansar()
# mi_mago.lanzar_hechizo()

# print("\nAcciones del guerrero")

# mi_guerrero.caminar()
# mi_guerrero.descansar()
# mi_guerrero.bloquear_ataque()


class Persona:
    def __init__(self, nombre):
        
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self,nombre_ingresado,nota_ingresada):
        super().__init__(nombre_ingresado)
        self.nota= nota_ingresada

def mostrar_info(self):
    print(f"Hola mi nombre es: {self.nombre} y mi nota es: {self.nota}")

    estudiante1= Estudiante("Juan", 8.5)
    estudiante1.mostrar_info()
