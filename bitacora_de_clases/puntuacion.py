 



def determinar_dia(numero: int):
    if numero < 0 or numero > 7:
        print("Numero invalido")
    else:
        if numero == 1:
           Dia = "Lunes"
        elif numero == 2:
            Dia = "Martes"
        elif numero == 3:
            Dia = "Miercoles"
        elif numero == 4:
            Dia = "Jueves"
        elif numero == 5:
            Dia = "viernes"
        elif numero == 6:
            Dia  = "Sabado"
        else:
            Dia = "domingo"
        return Dia
    



def convertir_puntuacion(puntaje: int):
    if puntaje < 0 or puntaje > 100:
        print("Puntaje invalido")
    else:
        if puntaje >= 90:
            Nota = "A"
        elif puntaje >=80:
            Nota = "B"
        elif puntaje >= 70:
            Nota = "c"
        elif puntaje >=60:
            Nota = "D"
        else:
            Nota = "F"
        return Nota
    pass

def main():
    puntaje = int(input("Ingrese el puntaje: "))
    Nota = convertir_puntuacion (puntaje)
    print (f"{puntaje} Puntos, equivalen a {Nota}")
    numero = int(input("Ingrese un Numero del 1 al 7 : "))
    Dia = determinar_dia (numero)
    print (f"EL {numero } Es dia es: {Dia} ")

if __name__ == "__main__": 
    main()