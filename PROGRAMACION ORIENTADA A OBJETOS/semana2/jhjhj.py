class AireAcondicionado:
    def __init__(self):
        self.temperatura=24
    
    def bajar_temperatura(self,grados):
        
        nueva_temperatura= self.temperatura - grados

        if nueva_temperatura <16:
            print("ERROR:La temperatura no puede bajar de 16 grados")

        else:
            self.temperatura= nueva_temperatura
            
            print("Temperatura actual:", self.temperatura)

aire1= AireAcondicionado()



aire1.bajar_temperatura(20)


