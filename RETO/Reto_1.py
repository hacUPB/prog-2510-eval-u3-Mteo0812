def informacion_usuario():
    Titulo = input("Ingrese el Titulo (Sr. o Sra.): ")
    Nombre = input("Ingrese su Nombre: ")
    Apellido = input("Ingrese su Apellido: ")
    print(f"Hola {Titulo} {Nombre} {Apellido}, !Bienvenido a Travis Airlines!.")
    return Titulo, Nombre, Apellido


def seleccionar_vuelo():
    Ciudades = ["Lima", "Bogotá", "Santiago", "Buenos Aires"]
    print("Seleccione su destino:")
    for i, Ciudad in (Ciudades,1):
        print(f"{i}. {Ciudad}")
    origen = Ciudades[int(input("Ingrese su ciudad de origen: "))-1]
    destino = Ciudades[int(input("Ingrese su ciudad de destino: "))-1]
    print(f"Su vuelo es de {origen} a {destino}.")
    return origen, destino


def main():
    print("Bienvenido a Travis Airlines")
    print("Por favor, ingrese su información personal.")
    Titulo, Nombre, Apellido = informacion_usuario()
    


if __name__ == "__main__":
    main()
