print("Bienvenido al sistema de compra de minutos para el laboratorio 3D")
nombre= input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))
autorizacion= input("tiene autorizacion de su profesor (si/no): ")
if edad>=15 and autorizacion =="si":
    print(f"{nombre} usted esta autorizado para ingresar al laboratorio")
    
    saldo_disponible = float(input("Ingrese su saldo disponible para comprar minutos: "))
    comprar_minutos = input("¿Desea comprar minutos para el laboratorio? (si/no): ")
    if comprar_minutos == "si":
        precio_paquete= float(input("Ingrese el precio del paquete de minutos: "))
        if saldo_disponible >= precio_paquete:
            saldo_disponible -= precio_paquete
            print(f"Compra exitosa")
            input("desea comprar otro paquete de minutos? (si/no): ")
            for articulo in range(4):
                desea_comprar = input("desea comprar otro? (si/no): ")
                if desea_comprar == "si":
                    precio=float(input("Ingrese el precio del articulo: "))
                    saldo_disponible -= precio
                    print(f"Compra exitosa. Saldo restante: {saldo_disponible}")
                    print("El total de articulos comprados es de: ", desea_comprar)

                else:
                    print("No se realizó la compra.")


        else:
            print("Saldo insuficiente para realizar la compra.")
      
    else:
        print("El estudiante no desea comprar minutos para el laboratorio.")
    

else:
    print(f"{nombre} usted no esta autorizado para ingresar al laboratorio")
    
    


