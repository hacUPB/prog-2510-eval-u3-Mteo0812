def mcd (num, den):
    if num <= den:
        menor = den
    else:
        menor = den
    for divisor in range (menor, 0, -1):
        if num % divisor == 0 and den % divisor == 0:
            max_com_div = divisor
            break
    return max_com_div

def fraccion_simplificada (num,den, maximo):
    sim= (num % maximo)
    pass

def Resultado (num, den):
    Resultado = num % den
    print(f"Reciduo: {Resultado}")

def imprimirr_fraccion(num, den, maximo):
   
    print(f"Fraccion: {num}/{den}")

def main():
    numerador = int(input("Ingrese el numerador: "))
    denominador= int(input("Ingrese el denominador: "))
    maximo = mcd(numerador, denominador)
    print(f"M.C.D = {maximo}")
    imprimirr_fraccion(numerador, denominador, maximo)
    Resultado(numerador,denominador)
if __name__ == "__main__":
    main()
