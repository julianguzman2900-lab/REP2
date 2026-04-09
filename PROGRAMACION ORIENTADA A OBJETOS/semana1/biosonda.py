 
class BioSonda:  #Creamos la clase BioSonda

    
    def __init__(self, numero_serie, ubicacion): # Creamos el constructor, para poder evitar definir todas las variables una por una y hacer el codigo mas corto
        self.numero_serie = numero_serie
        self.ubicacion = ubicacion
        self.energia = 100
        self.esta_activa = False

   
    def activar(self): # creeamos el metodo activar para verificar si la biosonda se encuentra apagada o encendida
        self.esta_activa = True

    
    def realizar_lectura(self, temperatura):# creamos el metodo lectura de temperatura para que verifique la temperaturo de la biosonda

        # Verifica si la biosonda está apagada
        if not self.esta_activa:
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
print("Energía restante:, {sonda.energia} %")
sonda.recargar()
print("Energía después de recargar:", sonda.energia)