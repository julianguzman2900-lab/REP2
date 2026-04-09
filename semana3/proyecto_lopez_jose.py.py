def ingresar_codigos ():
    lista = []
    while True:
        codigo = input("Ingrese un código de producto (o 'fin' para terminar): ")
        if codigo == 'fin':
            if codigo != 5:
                
                print("Dato invalido",+(codigo))
                continue
            break
            
        lista.append(codigo)
    return lista 


lote= int[0]
produccion: int[0,0,0]
entrega= int[0]

def procesar_codigos(codigo):
    for codigo in codigo:""