class DronVigilancia:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = 100
        self.estado = "En tierra"

    def despegar(self):
        if self.estado == 'En tierra':
            if self.bateria >= 25:
                self.estado = "En vuelo"
                print("¡Despegue exitoso! El dron ahora está en el aire.")
            else:
                print("[ERROR: Batería insuficiente para despegar]")
        else:
            print("[ERROR: El dron ya está en vuelo]")

    def patrullar(self):
        if self.estado == "En vuelo":
            self.bateria -= 30
            if self.bateria < 0:
                self.bateria = 0

            print(f"Patrullaje completado. Bateria usada 30%. Batería restante: {self.bateria}%")

            if self.bateria < 10:
                self.estado = "En tierra"
                print("¡Batería crítica! El dron aterrizó automáticamente.")
        else:
            print("[ERROR: El dron no puede patrullar si está en tierra]")

    def recargar(self):
        if self.estado == "En tierra":
            self.bateria = 100
            print("Recargando...")
            print("Dron recargado al 100%")
        else:
            print("[ERROR: No se puede recargar el dron en vuelo]")

    def estado_actual(self):
        print(f"\n--- ESTADO ACTUAL: {self.nombre} [{self.modelo}] ---")
        print(f"Batería: {self.bateria}% | Estado: {self.estado}\n")


print(">>> INICIANDO SISTEMA SKYWATCH <<<")

nombre = input("Ingrese nombre del dron: ")
modelo = input("Ingrese modelo del dron: ")

dron = DronVigilancia(nombre, modelo)

while True:
    dron.estado_actual()
    opcion = input("¿Qué acción desea realizar? (1. Despegar / 2. Patrullar / 3. Recargar / 4. Salir): ")

    if opcion == "1":
        dron.despegar()
    elif opcion == "2":
        dron.patrullar()
    elif opcion == "3":
        dron.recargar()
    elif opcion == "4":
        print("Apagando sistema...")
        break
    else:
        print("Opción inválida")
