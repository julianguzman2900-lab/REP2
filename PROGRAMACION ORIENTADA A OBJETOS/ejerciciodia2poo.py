
class BioSonda:#Creamos la clase BioSonda

    # Constructor de la clase
    def __init__(self, numero_serie, ubicacion):# Creamos el constructor, para poder evitar definir todas las variables una por una y hacer el codigo mas corto
        self.numero_serie = numero_serie
        self.ubicacion = ubicacion
        self.energia = 100
        self.esta_activa = False

    # Método para activar la biosonda
    def activar(self):
        self.esta_activa = True

    # Método para realizar una lectura de temperatura
    def realizar_lectura(self, temperatura):

        # Verifica si la biosonda está apagada
        if self.esta_activa == False:
            return "Error: la biosonda está apagada."

        # Verifica si la energía es menor al 15%
        if self.energia < 15:
            return "Batería baja. Recargue la biosonda."

        # Resta 10% de energía por cada lectura
        self.energia -= 10

        # Retorna el informe de lectura
        return f"Temperatura registrada: {temperatura}°C en {self.ubicacion}"

    # Método para recargar la energía
    def recargar(self):
        self.energia = 100


# Ejemplo de uso
sonda = BioSonda("BS-001", "Laboratorio Central")

print(sonda.realizar_lectura(25))
sonda.activar()
print(sonda.realizar_lectura(25))
print("Energía restante,{sonda.energia}%")
