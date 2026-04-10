class SensorPresion :  #Crea la clase SensorPresion
    limite_peligro= 200
    total_lecturas= 0
                        #Definimos los atributos globales,limite_peligro y total_lecturas
    def __init__(self,nombre,presion): #creamos el constructor con dos parametros nombre y presion
        self.nombre=nombre     
        self.__presion=presion     #creamos los atributos individuales self.nombre y el atributo privado self.__presion
        SensorPresion.total_lecturas+=1 #Aqui indicamos que sume 1 al atributo global 



    @property  
    def presion(self):  # usamos @property para poder retornar el atributo privado self.__presion
        return self.__presion
    
    @presion.setter  #Usamos el modificador de atributos privados setter
    def presion(self, nueva_presion):
        if nueva_presion > 0:        
            self.__presion = nueva_presion #en este if le pido que valide si la presion leida es mayor a 0 para poder modificar el atributo privado
        else:
            self.__presion = 0
            print("[ERROR] LA PRESION DEBE SER MAYOR A 0")
            #Aqui indico que si no se cumple la validacion anterior, indique que la presion no puede ser menor a 0



print("---- SISTEMA DE MONITOREO INDUSTRIAL ----")
print("Leyendo registros de presion...") #imprimo  el encabezado del programa para una mejor estetica
with open("registro.txt", "r") as archivo: # aqui pido que se lea el archivo con extension "registro.txt"
    lista_sensores = [] # Creo una variable en la que se almacenaran la cantidad de sensores que se revisaran  
    while True:
        nombre= archivo.readline().strip() #Creo un while en el que lea la primer linea del archivo con readline() y la almacene en nombre

        if nombre=="": #si la linea esta vacia el programa termina
            break


        presion_texto=archivo.readline().strip()
        presion_numero= int(presion_texto) #aqui pido que lea el texto 


        sensor = SensorPresion(nombre,presion_numero)

        lista_sensores.append(sensor)
with open("alertas.txt","w") as archivo_alertas:
    archivo_alertas.write("REPORTE DE INCIDENCIAS - CALDERAS CRITICAS\n")
    archivo_alertas.write("-------------------------------------------\n")

    contador_alertas= 1
    
    for sensor in lista_sensores:
        if sensor.presion > SensorPresion.limite_peligro:
            estado= "¡PELIGRO!"
            archivo_alertas.write(f"{contador_alertas}. {sensor.nombre}\n")
            contador_alertas+= 1

        else:
            estado= "SEGURO"


        print(f"Analizando:{sensor.nombre}| Estado:{estado}")

print("\n[AUDITORÍA] Se han generado alertas en el archivo 'alertas.txt'")
print(f"[RESUMEN] Total de sensores procesados: {SensorPresion.total_lecturas}.")
print("---------------------------------------")

