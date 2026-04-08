class RegistroAcademico:
    def __init__(self,nombre_alumno,nota_inicial):

        self.nombre= nombre_alumno
        self.__nota= nota_inicial
        self.cuenta_activa= True

    def get_nota(self):
     return self.__nota
        
    def bloquear_cuenta(self):
        self.cuenta_activa = False
    
    def set_nota(self,nueva_nota):
     if  self.cuenta_activa==False:
          return -2
     elif 0>= nueva_nota <=100:
            return 1
     else:
         return -1
     
print(">>>> Registro Academico <<<<")
     
nota_alumno=RegistroAcademico("Laura",85)

intentos_permitidos=3

while intentos_permitidos>0:
    int(input("Ingrese la nueva nota: "))

    
        

     
