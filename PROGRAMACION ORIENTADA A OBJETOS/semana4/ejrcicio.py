# from abc import ABC, abstractmethod


# class FuenteEnergia(ABC):
#     def __init__(self, id_generador, capacidad_maxima, nombre):
#         self.id_generador = id_generador
#         self.capacidad_maxima = capacidad_maxima
#         self.nombre = nombre
#         self.produccion_actual = 0.0

#     @abstractmethod
#     def generar(self, valor_entrada):
#         pass

# class PanelSolar(FuenteEnergia):
#     def __init__(self, id_generador, capacidad_maxima):
#         super().__init__(id_generador, capacidad_maxima, "Panel Solar")

#     def generar(self, clima):
#         if clima == "Soleado":
#             self.produccion_actual = self.capacidad_maxima
#         else:
#             self.produccion_actual = 0.0
#         return self.produccion_actual

# class TurbinaEolica(FuenteEnergia):
#     def __init__(self, id_generador, capacidad_maxima):
#         super().__init__(id_generador, capacidad_maxima, "Turbina Eólica")

#     def generar(self, velocidad_viento):
#         produccion = float(velocidad_viento) * 5
#         if produccion > self.capacidad_maxima:
#             self.produccion_actual = self.capacidad_maxima
#         else:
#             self.produccion_actual = produccion
#         return self.produccion_actual

# class GeneradorDiesel(FuenteEnergia):
#     def __init__(self, id_generador, capacidad_maxima, combustible):
#         super().__init__(id_generador, capacidad_maxima, "Motor Diesel")
#         self.combustible = combustible

#     def generar(self, _):
#         if self.combustible > 0:
#             self.combustible -= 10.0
#             self.produccion_actual = self.capacidad_maxima
#         else:
#             self.produccion_actual = 0.0
#         return self.produccion_actual


# class FabricaEnergia:
#     registro_energia = {
#         "solar": PanelSolar,
#         "eolica": TurbinaEolica,
#         "diesel": GeneradorDiesel
#     }

#     @staticmethod
#     def crear_generador(datos_del_generador):
#         if "tipo" in datos_del_generador:
#             tipo_de_energia = datos_del_generador["tipo"]
            
#             if tipo_de_energia in FabricaEnergia._registro_energias:
#                 modelo = FabricaEnergia._registro_energias[tipo_de_energia]
                
            
#                 id_generador = datos_del_generador["id_generador"]
#                 capacidad_maxima = datos_del_generador["capacidad_maxima"]
                
               
#                 if tipo_de_energia == "diesel":
#                     if "combustible" in datos_del_generador:
#                         litros = datos_del_generador["combustible"]
#                     else:
#                         litros = 0.0
                
#                     return modelo(id_generador, capacidad_maxima, litros)
                
              
#                 return modelo(id_generador, capacidad_maxima)
        
#         return False


# class InterfazRed:
#     def mostrar_tablero(self, lista_de_generadores):
#         print("\n" + "o" + "-" * 45 + "o")
#         print("|        TABLERO DE CONTROL ENERGÉTICO        |")
#         print("o" + "-" * 45 + "o")
        
#         for generador_activo in lista_de_generadores:
           
#             informacion_generador = f"{generador_activo.nombre} ({generador_activo.id_generador}): {generador_activo.produccion_actual} kW"
#             print(f"| {informacion_generador} |")
            
#         print("o" + "-" * 45 + "o\n")

#     def solicitar_clima(self):
#         return input("Ingrese el clima (Soleado/Nublado): ")

#     def solicitar_viento(self):
#         return input("Ingrese velocidad del viento (km/h): ")

#     def mostrar_mensaje_error(self, texto_error):
#         print(f"ERROR: {texto_error}")


# class ControladorEnergia:
#     def __init__(self):
#         self.vista_sistema = InterfazRed()
#         self.lista_de_generadores = []

#     def cargar_datos(self, lista_de_datos):
    
#         for objeto in lista_de_datos:
#             objeto_creado = FabricaEnergia.crear_generador(objeto)
#             if objeto_creado != False:
#                 self.lista_de_generadores.append(objeto_creado)

#     def iniciar_programa(self):
  
#         clima_es_valido = False
#         clima_usuario = ""
#         while clima_es_valido == False:
#             clima_usuario = self.vista_sistema.solicitar_clima()
#             if clima_usuario == "Soleado":
#                 clima_es_valido = True
#             if clima_usuario == "Nublado":
#                 clima_es_valido = True
#             if clima_es_valido == False:
#                 self.vista_sistema.mostrar_mensaje_error("Use 'Soleado' o 'Nublado'.")

      
#         viento_usuario = 0.0
#         es_dato_valido = False
#         while es_dato_valido == False:
#             try:
#                 viento_usuario = float(self.vista_sistema.solicitar_viento())
#                 es_dato_valido = True
#             except ValueError:
#                 self.vista_sistema.mostrar_mensaje_error("Ingrese un número.")

#         for generador_a_procesar in self.lista_de_generadores:
#             if isinstance(generador_a_procesar, PanelSolar):
#                 generador_a_procesar.generar(clima_usuario)
#             elif isinstance(generador_a_procesar, TurbinaEolica):
#                 generador_a_procesar.generar(viento_usuario)
#             elif isinstance(generador_a_procesar, GeneradorDiesel):
#                 generador_a_procesar.generar("")

#         self.vista_sistema.mostrar_tablero(self.lista_de_generadores)

# if __name__ == "__main__":
   
#     datos_de_entrada = [
#         {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
#         {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
#         {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
#     ]
    
#     control = ControladorEnergia()
    # control.cargar_datos(datos_de_entrada)
    # control.iniciar_programa()



from abc import ABC, abstractmethod


class NucleoEnergia:
    def __init__(self, nivel_energia_inicial):
        self.nivel_energia = nivel_energia_inicial

    def __str__(self):
        return f"{self.nivel_energia}%"

class NaveEspacial(ABC):
    conteo_total_naves_creadas = 0 

    def __init__(self, nombre_nave, codigo, energia_inicial, tipo_nave):
        self.nombre = nombre_nave
        self.codigo = codigo
        self.tipo = tipo_nave 
        self._energia = NucleoEnergia(energia_inicial)
        self._nivel_escudos = 100
        NaveEspacial.conteo_total_naves_creadas += 1

    @property
    def nivel_energia_actual(self):
        return self._energia.nivel_energia

    @nivel_energia_actual.setter
    def nivel_energia_actual(self, nuevo_valor):
        if nuevo_valor > 100:
            self._energia.nivel_energia = 100
        elif nuevo_valor < 0:
            self._energia.nivel_energia = 0
        else:
            self._energia.nivel_energia = nuevo_valor

    @abstractmethod
    def mision(self, cantidad_energia_consumo):
        pass

    def __lt__(self, otra_nave):
        return self.nivel_energia_actual < otra_nave.nivel_energia_actual

    def __str__(self):
        return (f"Nave: {self.nombre} | Tipo: {self.tipo} | Código: {self.codigo} | "
                f"Energía: {self.nivel_energia_actual}% | Escudos: {self._nivel_escudos}%")

class NaveCombate(NaveEspacial):
    def __init__(self, nombre_nave, codigo, energia_inicial, potencia):
        super().__init__(nombre_nave, codigo, energia_inicial, "Combate")
        self.potencia = potencia

    def mision(self, consumo_energia):
        if self.nivel_energia_actual >= consumo_energia:
            self.nivel_energia_actual -= consumo_energia
            self._nivel_escudos -= 20
            if self._nivel_escudos < 0:
                self._nivel_escudos = 0
            return f"Resultado: Ataque desplegado (Potencia {self.potencia}). Escudos: {self._nivel_escudos}%."
        else:
            return "Error: Energía insuficiente para combate."

class NaveCarga(NaveEspacial):
    def __init__(self, nombre_nave, codigo, energia_inicial, capacidad):
        super().__init__(nombre_nave, codigo, energia_inicial, "Carga")
        self.capacidad = capacidad

    def mision(self, consumo_energia):
        if self.nivel_energia_actual >= consumo_energia:
            self.nivel_energia_actual -= consumo_energia
            return f"Resultado: Transportando {self.capacidad} toneladas."
        else:
            return "Error: Energía insuficiente para transporte."

class NaveHibrida(NaveCombate, NaveCarga):
    def __init__(self, nombre_nave, codigo, energia_inicial, potencia, capacidad):
        NaveEspacial.__init__(self, nombre_nave, codigo, energia_inicial, "Hibrida")
        self.potencia = potencia
        self.capacidad = capacidad

    def mision(self, consumo_energia):
        if self.nivel_energia_actual >= consumo_energia:
            self.nivel_energia_actual -= consumo_energia
            self._nivel_escudos -= 30
            if self._nivel_escudos < 0:
                self._nivel_escudos = 0
            return f"Resultado Híbrido: Escudos al {self._nivel_escudos}%."
        else:
            return "Error: Energía insuficiente."

def iniciar_sistema():
    naves_listado = []
    print(">>> ESTACIÓN ESPACIAL AETHELGARD ACTIVADA <<<")
    
    while True:
        print("\n1. Registrar | 2. Misión | 3. Comparar | 4. Fusionar | 5. Stat | 6. Salir")
        opcion = input("Seleccione acción: ")

        if opcion == "1":
            tipo_entrada = input("Tipo (1.Combate, 2.Carga, 3.Híbrida): ")
            while True:
                nombre_nuevo = input("Nombre de la nave: ")
                nombre_incorrecto = False
                for letra in nombre_nuevo:
                    try:
                        int(letra)
                        nombre_incorrecto = True
                    except ValueError:
                        pass
                if nombre_incorrecto == False:
                    break
                else:
                    print("[ERROR] El nombre no debe contener números.")
            
            codigo = input("Código: ")
            try:
                if tipo_entrada == "1":
                    valor_potencia = int(input("Potencia: "))
                    naves_listado.append(NaveCombate(nombre_nuevo, codigo, 100, valor_potencia))
                elif tipo_entrada == "2":
                    valor_capacidad = int(input("Capacidad: "))
                    naves_listado.append(NaveCarga(nombre_nuevo, codigo, 100, valor_capacidad))
                elif tipo_entrada == "3":
                    valor_potencia = int(input("Potencia: "))
                    valor_capacidad = int(input("Capacidad: "))
                    naves_listado.append(NaveHibrida(nombre_nuevo, codigo, 100, valor_potencia, valor_capacidad))
                
                if tipo_entrada == "1" or tipo_entrada == "2" or tipo_entrada == "3":
                    print(f"Éxito. Total naves fabricadas: {NaveEspacial.conteo_total_naves_creadas}")
                else:
                    print("[ERROR] Tipo de nave no válido.")
            except ValueError:
                print("[ERROR] Los valores deben ser números enteros.")

        elif opcion == "2":
            if naves_listado:
                for posicion, nave_actual in enumerate(naves_listado):
                    print(f"[{posicion}] {nave_actual.nombre} ({nave_actual.tipo})")
                try:
                    posicion_seleccionada = int(input("Elija la nave para realizar misión: "))
                    energia_consumida = int(input("Energía a consumir: "))
                    print(naves_listado[posicion_seleccionada].mision(energia_consumida))
                except (ValueError):
                    print("[ERROR] Selección o consumo inválido.")
            else:
                print("Hangar vacío.")

        elif opcion == "3":
            if len(naves_listado) >= 2:
                for posicion, nave_actual in enumerate(naves_listado):
                    print(f"[{posicion}] {nave_actual.nombre} (Energía: {nave_actual.nivel_energia_actual}%)")
                try:
                    nave1 = int(input("Elija la primera nave: "))
                    nave2 = int(input("Elija la segunda nave: "))
                    if naves_listado[nave1] < naves_listado[nave2]:
                        print(f"Resultado: {naves_listado[nave2].nombre} tiene más energía.")
                    elif naves_listado[nave2] < naves_listado[nave1]:
                        print(f"Resultado: {naves_listado[nave1].nombre} tiene más energía.")
                    else:
                        print("Resultado: Tienen la misma energía.")
                except (ValueError, IndexError):
                    print("[ERROR] Índices inválidos.")
            else:
                print("Se necesitan al menos 2 naves.")

        elif opcion == "4":
            
            pass

        elif opcion == "5":
            for posicion, nave_imprimir in enumerate(naves_listado):
                print(f"[{posicion}] {nave_imprimir}")
        
        elif opcion == "6":
            print("Cerrando estación...")
            break

if __name__ == "__main__":
    iniciar_sistema()
