print("Tarifario hotel buena vista")
nombre_huesped = input("Ingrese el nombre del huésped: ")
temporada = input("Ingrese la temporada (alta/media/baja): ")
noches = int(input("Ingrese el número de noches que se quedara: "))
precio= float(input("Ingrese el precio base popor noche: "))
membresia = input("¿El huésped tiene membresía? (si/no): ")

match temporada:
    case "alta":
        