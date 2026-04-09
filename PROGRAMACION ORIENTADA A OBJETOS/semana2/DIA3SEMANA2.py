# class TermostatoDigital:
#     def __init__(self):
#         self.__temperatura=0
#         self.termostato_activo= False

#     def encendido(self):
#         if self.termostato_activo== False:
#             self.termostato_activo= True 

#         else:
#             self.termostato_activo= False

#     @property
#     def temperatura(self):
#         return self.__temperatura
    

#     @temperatura.setter
#     def temperatura(self,nueva_temperatura):
#         if  16<nueva_temperatura >35:
            
#             print("Temperatura invalida") 
            
#         else:
#             self.__temperatura= nueva_temperatura
#             print("La temperatura que ha ingresado es valida")
         
class RegistroVisitantes:

    total_personas=0

    def __init__(self, nombre_visitante):
        self.nombre=nombre_visitante

        RegistroVisitantes.total_personas+=1
        
        print(f"{self.nombre} ha ingresado. La pizarra global ahora marca : {RegistroVisitantes.total_personas} ")



persona1=RegistroVisitantes("Maria")

persona2= RegistroVisitantes("Carlos")

persona3=RegistroVisitantes("Julian")

print(f"\nTotal final del dia de personas es: {RegistroVisitantes.total_personas}")