def sim_desintegracion_orbital(alt_inicial, coef_arrastre_inicial, alt_minima):
    alt_actual = alt_inicial
    coef_arrastre = coef_arrastre_inicial
    orbitas = 0

    print("\nSimulando la desintegración orbital...")

    while True:
 
        alt_perdida = coef_arrastre * alt_actual
        alt_actual -= alt_perdida  
        orbitas += 1

        print(f"Órbita {orbitas}: Altitud actual = {alt_actual:.2f} km, Coeficiente de arrastre = {coef_arrastre:.4f}")

        coef_arrastre += 0.0001

        
        if alt_actual < alt_minima:
            print(f"\nEl satélite ha reingresado en la atmósfera terrestre después de {orbitas} órbitas.")
            print(f"Altitud final: {alt_actual:.2f} km")
            break

        if alt_perdida < 0.01:
            print(f"\nEl satélite se ha estabilizado en una órbita baja después de {orbitas} órbitas.")
            print(f"Altitud final: {alt_actual:.2f} km")
            break

def main():
    print("Simulación de desintegración orbital de un satélite")

    alt_inicial_texto = input("Ingrese la altitud inicial del satélite (en kilómetros): ")
    coef_arrastre_texto = input("Introduzca el coeficiente de arrastre inicial (ej. 0.01): ")
    alt_minima_texto = input("Ingrese la altitud mínima segura (en kilómetros): ")
    # En esta parte investigue sobre el usuo de estos comandos para poder validar y que el sistema no se bloque si el usuario no ingre un valor correcto
    if alt_inicial_texto.replace('.', '', 1).isdigit() and \
       coef_arrastre_texto.replace('.', '', 1).isdigit() and \
       alt_minima_texto.replace('.', '', 1).isdigit():

        alt_inicial = float(alt_inicial_texto)
        coef_arrastre_inicial = float(coef_arrastre_texto)
        alt_minima = float(alt_minima_texto)

        if alt_inicial <= 0:
            print("La altitud inicial debe ser mayor que cero.")
            return
        if coef_arrastre_inicial <= 0:
            print("El coeficiente de arrastre debe ser mayor que cero.")
            return
        if alt_minima <= 0:
            print("La altitud mínima debe ser mayor que cero.")
            return
        if alt_minima >= alt_inicial:
            print("La altitud mínima debe ser menor que la altitud inicial.")
            return
        
        sim_desintegracion_orbital(alt_inicial, coef_arrastre_inicial, alt_minima)

    else:
        print("Entrada inválida. Asegúrate de escribir solo números.")

main()
