
#Quiz 25/03/2025

Num_secreto=15
print("¡Bienvenido al juego adivina el numero!")
print("Tienes que adivinar un numero entre 1 y 100")
Intento = 0
Num_intentos = 0
#error no ingrese el dentro del bucle while la variable "Intentos"
while Intento != Num_secreto: # Puse el in en vez del != que diferencia cada variable y puse un rango lo que hace que el programa no arranque 
    Intento = int(input("Ingrese su intento: "))
    Num_intentos += 1
# Utilice else em vez de if 
    if Intento > Num_secreto:
        print("el numero es menor. Intente de nuevo.")
    elif Intento < Num_secreto:
        print("El numeor es mayor. Intente de nuevo")
print(f"Felicidades Has adivinado el numero en {Num_intentos} intentos") # Me falto poner f antes de iniciar con el texto 

#este seria el codigo correcto puesto que en el que realice en la evaluacion ingres por fuera del bucle las condiciones y por ende el codigo ya no corria