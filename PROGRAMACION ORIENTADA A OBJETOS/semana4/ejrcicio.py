from abc import ABC, abstractmethod


class FuenteEnergia(ABC):
    def __init__(self, id_generador, capacidad_maxima, nombre):
        self.id_generador = id_generador
        self.capacidad_maxima = capacidad_maxima
        self.nombre = nombre
        self.produccion_actual = 0.0

    @abstractmethod
    def generar(self, valor_entrada):
        pass

class PanelSolar(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima):
        super().__init__(id_generador, capacidad_maxima, "Panel Solar")

    def generar(self, clima):
        if clima == "Soleado":
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual

class TurbinaEolica(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima):
        super().__init__(id_generador, capacidad_maxima, "Turbina Eólica")

    def generar(self, velocidad_viento):
        produccion = float(velocidad_viento) * 5
        if produccion > self.capacidad_maxima:
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = produccion
        return self.produccion_actual

class GeneradorDiesel(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima, combustible):
        super().__init__(id_generador, capacidad_maxima, "Motor Diesel")
        self.combustible = combustible

    def generar(self, _):
        if self.combustible > 0:
            self.combustible -= 10.0
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual


class FabricaEnergia:
    registro_energia = {
        "solar": PanelSolar,
        "eolica": TurbinaEolica,
        "diesel": GeneradorDiesel
    }

    @staticmethod
    def crear_generador(datos_del_generador):
        if "tipo" in datos_del_generador:
            tipo_de_energia = datos_del_generador["tipo"]
            
            if tipo_de_energia in FabricaEnergia._registro_energias:
                modelo = FabricaEnergia._registro_energias[tipo_de_energia]
                
            
                id_generador = datos_del_generador["id_generador"]
                capacidad_maxima = datos_del_generador["capacidad_maxima"]
                
               
                if tipo_de_energia == "diesel":
                    if "combustible" in datos_del_generador:
                        litros = datos_del_generador["combustible"]
                    else:
                        litros = 0.0
                
                    return modelo(id_generador, capacidad_maxima, litros)
                
              
                return modelo(id_generador, capacidad_maxima)
        
        return False


class InterfazRed:
    def mostrar_tablero(self, lista_de_generadores):
        print("\n" + "o" + "-" * 45 + "o")
        print("|        TABLERO DE CONTROL ENERGÉTICO        |")
        print("o" + "-" * 45 + "o")
        
        for generador_activo in lista_de_generadores:
           
            informacion_generador = f"{generador_activo.nombre} ({generador_activo.id_generador}): {generador_activo.produccion_actual} kW"
            print(f"| {informacion_generador} |")
            
        print("o" + "-" * 45 + "o\n")

    def solicitar_clima(self):
        return input("Ingrese el clima (Soleado/Nublado): ")

    def solicitar_viento(self):
        return input("Ingrese velocidad del viento (km/h): ")

    def mostrar_mensaje_error(self, texto_error):
        print(f"ERROR: {texto_error}")


class ControladorEnergia:
    def __init__(self):
        self.vista_sistema = InterfazRed()
        self.lista_de_generadores = []

    def cargar_datos(self, lista_de_datos):
    
        for objeto in lista_de_datos:
            objeto_creado = FabricaEnergia.crear_generador(objeto)
            if objeto_creado != False:
                self.lista_de_generadores.append(objeto_creado)

    def iniciar_programa(self):
  
        clima_es_valido = False
        clima_usuario = ""
        while clima_es_valido == False:
            clima_usuario = self.vista_sistema.solicitar_clima()
            if clima_usuario == "Soleado":
                clima_es_valido = True
            if clima_usuario == "Nublado":
                clima_es_valido = True
            if clima_es_valido == False:
                self.vista_sistema.mostrar_mensaje_error("Use 'Soleado' o 'Nublado'.")

      
        viento_usuario = 0.0
        es_dato_valido = False
        while es_dato_valido == False:
            try:
                viento_usuario = float(self.vista_sistema.solicitar_viento())
                es_dato_valido = True
            except ValueError:
                self.vista_sistema.mostrar_mensaje_error("Ingrese un número.")

        for generador_a_procesar in self.lista_de_generadores:
            if isinstance(generador_a_procesar, PanelSolar):
                generador_a_procesar.generar(clima_usuario)
            elif isinstance(generador_a_procesar, TurbinaEolica):
                generador_a_procesar.generar(viento_usuario)
            elif isinstance(generador_a_procesar, GeneradorDiesel):
                generador_a_procesar.generar("")

        self.vista_sistema.mostrar_tablero(self.lista_de_generadores)

if __name__ == "__main__":
   
    datos_de_entrada = [
        {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
        {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
        {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
    ]
    
    control = ControladorEnergia()
    control.cargar_datos(datos_de_entrada)
    control.iniciar_programa()
