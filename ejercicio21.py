try:
    fn = float(input("ingrese un numero:"))
    sn = float(input("ingrese otro numero:"))
    suma = fn+sn
    resta = fn-sn
    multiplicacion = fn*sn
    try:
        division = fn/sn

        print("la suma de los numeros es:",suma)
        print("la resta de los numeros es:",resta)
        print("la multiplicacion de los numeros es:",multiplicacion)
        print("la division de los numeros es:",division)
    except:
        print("el divisor no puede ser 0")
except:
    print("No ingreses letras ni simbolos")