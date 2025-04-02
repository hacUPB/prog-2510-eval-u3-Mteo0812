import random

def informacion_usuario():
    Titulo = input("Ingrese el Titulo (Sr. o Sra.): ")
    Nombre = input("Ingrese su Nombre: ")
    Apellido = input("Ingrese su Apellido: ")
    print(f"Hola {Titulo} {Nombre} {Apellido}, ¡Bienvenido a Travis Airlines!.")
    return Titulo, Nombre, Apellido


def seleccionar_vuelo():
    ciudades = ["Santa Marta", "Bogotá", "Santiago", "San Andres", "Caracas"]
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    distancias = [(("Santa Marta", "Bogotá"), 830), (("Santa Marta", "Santiago"), 989),
        (("Santa Marta", "San Andres"), 968), (("Santa Marta", "Caracas"), 1412),
        (("Bogotá", "Santiago"), 989), (("Bogotá", "San Andres"), 968), (("Bogotá", "Caracas"), 1412),
        (("Santiago", "San Andres"), 968), (("Santiago", "Caracas"), 1412),
        (("San Andres", "Caracas"), 1412)]
    
    print("Seleccione su ciudad de origen:")
    for i, ciudad in enumerate(ciudades,1):
        print(f"{i}. {ciudad}")
    origen = ciudades[int(input("Ingrese el número de su ciudad de origen: ")) - 1]
    
    print("Seleccione su ciudad de destino:")
    for i, ciudad in enumerate(ciudades,1):
        print(f"{i}. {ciudad}")
    destino = ciudades[int(input("Ingrese el número de su ciudad de destino: ")) - 1]
    
    if origen == destino:
        print("El origen y el destino no pueden ser iguales.")
        return seleccionar_vuelo()
    
    print("Seleccione el día de la semana:")
    for i, dia in enumerate(dias_semana, 1):
        print(f"{i}. {dia}")
    dia_semana_num = int(input("Ingrese el número del día de la semana (1-7): "))
    
    if not (1 <= dia_semana_num <= 7):
        print("El día de la semana no es válido.")
        return seleccionar_vuelo()
    
    dia_semana = dias_semana[dia_semana_num - 1]
    dia_mes = int(input("Ingrese el día del mes en el que desea viajar (1-31): "))
    
    if not (1 <= dia_mes <= 31):
        print("El día del mes no es válido.")
        return seleccionar_vuelo()
    
    distancia = 0
    for (ciudad1, ciudad2), km in distancias:
        if (origen == ciudad1 and destino == ciudad2) or (origen == ciudad2 and destino == ciudad1):
            distancia = km
            break
    
    if distancia < 400:
        precio = 79900 if dia_semana in ["lunes", "martes", "miércoles", "jueves"] else 119900
    else:
        precio = 156900 if dia_semana in ["lunes", "martes", "miércoles", "jueves"] else 213000

    print(f"Su vuelo es de {origen} a {destino}. Precio: ${precio:,.2f}")
    return origen, destino, dia_semana, dia_mes, precio


def asignar_asiento():
    print("Seleccione su preferencia de asiento:")
    print("1. Pasillo (Asiento C)")
    print("2. Ventana (Asiento A)")
    print("3. Sin preferencia (Asiento B)")
    
    opcion = int(input("Ingrese el número de su preferencia: "))
    if opcion == 1:
        letra_asiento = "C"
    elif opcion == 2:
        letra_asiento = "A"
    else:
        letra_asiento = "B"
    
    numero_asiento = random.randint(1, 29)
    asiento = f"{numero_asiento}{letra_asiento}"
    print(f"Su asiento asignado es: {asiento}")
    return asiento


def main():
    print("Bienvenido a Travis Airlines")
    print("Por favor, ingrese su información personal.")
    Titulo, Nombre, Apellido = informacion_usuario()
    origen, destino, dia_semana, dia_mes, precio = seleccionar_vuelo()
    asiento = asignar_asiento()
    print("\nResumen de su reserva:")
    print(f"Nombre: {Titulo} {Nombre} {Apellido}")
    print(f"Vuelo: {origen} -> {destino}")
    print(f"Fecha de viaje: {dia_semana} {dia_mes} del 2025")
    print(f"Precio del billete: ${precio:,.2f}")
    print(f"Asiento asignado: {asiento}")


if __name__ == "__main__":
    main()