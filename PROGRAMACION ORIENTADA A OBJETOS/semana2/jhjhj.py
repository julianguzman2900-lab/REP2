# class AireAcondicionado:
#     def __init__(self):
#         self.temperatura=24
    
#     def bajar_temperatura(self,grados):
        
#         nueva_temperatura= self.temperatura - grados

#         if nueva_temperatura <16:
#             print("ERROR:La temperatura no puede bajar de 16 grados")

#         else:
#             self.temperatura= nueva_temperatura
            
#             print("Temperatura actual:", self.temperatura)

# aire1= AireAcondicionado()



# aire1.bajar_temperatura(20)







# Clase que representa cada sensor de presión
# class SensorPresion:

#     # Atributos de clase
#     LIMITE_PELIGRO = 200
#     total_lecturas = 0

#     # Constructor
#     def __init__(self, nombre, presion):
#         self.nombre = nombre
#         self.presion = presion
#         SensorPresion.total_lecturas += 1

#     # Getter
#     @property
#     def presion(self):
#         return self.__presion

#     # Setter con validación
#     @presion.setter
#     def presion(self, nueva_presion):
#         if nueva_presion >= 0:
#             self.__presion = nueva_presion
#         else:
#             self.__presion = 0


# # Lista para guardar todos los sensores
# lista_sensores = []

# print("--- SISTEMA DE MONITOREO INDUSTRIAL ---")
# print("Leyendo registros de presión...")

# # Lectura del archivo
# with open("registros.txt", "r") as archivo:

#     while True:
#         nombre = archivo.readline().strip()

#         # Si ya no hay más líneas, termina el ciclo
#         if nombre == "":
#             break

#         presion_texto = archivo.readline().strip()
#         presion_numero = int(presion_texto)

#         # Crear objeto
#         sensor = SensorPresion(nombre, presion_numero)

#         # Guardar objeto en la lista
#         lista_sensores.append(sensor)

# # Escritura del archivo de alertas
# with open("alertas.txt", "w") as archivo_alertas:

#     archivo_alertas.write("REPORTE DE INCIDENCIAS - CALDERAS CRÍTICAS\n")
#     archivo_alertas.write("------------------------------------------\n")

#     contador_alertas = 1

#     # Recorrer la lista de sensores
#     for sensor in lista_sensores:

#         if sensor.presion > SensorPresion.LIMITE_PELIGRO:
#             estado = "¡PELIGRO!"
#             archivo_alertas.write(f"{contador_alertas}. {sensor.nombre}\n")
#             contador_alertas += 1
#         else:
#             estado = "Seguro"

#         print(f"Analizando: {sensor.nombre} | Estado: {estado}")

# print("\n[AUDITORÍA] Se han generado alertas en el archivo 'alertas.txt'")
# print(f"[RESUMEN] Total de sensores procesados: {SensorPresion.total_lecturas}.")
# print("---------------------------------------")