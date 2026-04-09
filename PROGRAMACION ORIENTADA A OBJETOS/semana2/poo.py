# class Cuenta:
#     def __init__ (self, saldo_inicial):
#         self.nombre= "Publica"
#         self._saldo=saldo_inicial



# mi_cuenta=Cuenta(1000)
# print(mi_cuenta.nombre)
# print(mi_cuenta._saldo)




archivo_prueba= open("archivo.text", "a")

archivo_prueba.write("Hoy aprendi a escribir a un archivo")

archivo_prueba.close()




# with open("archivo.text", "a")as archivo_prueba:
#     archivo_prueba.write("hoy aprendi a escribir en un archivo\n")
#     archivo_prueba.write("Ahora puedo escribir varias lineas\n")


# with open("archivo.text","r") as archivo_prueba:
#    print("contenido del archivo")
   
#    for linea in archivo_prueba:

#      texto_limpio= linea.strip()
#      print(f"->{texto_limpio}")
 ####



with open ("registro.text","r") as archivo_prueba:
    contador=0
    for linea in archivo_prueba:
            
            linea_limpia=linea.strip()
            contador+=1
            print(linea_limpia)
            
print(f"Total de líneas leídas: {contador}")