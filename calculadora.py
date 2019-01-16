def menu():
    print("---SELECCIONE UNA OPCIÓN---")
    print("1- Sumar-")
    print("2- Restar-")
    print("3- Multiplicar-")
    print("4- Dividir-")
    print("5- Finlalizar programa")
    leer_opcion()

def leer_opcion():
    try:
        opcion = int(input(">>>"))
        if(opcion<1 or opcion>5):
            print("seleccionaste una opcion fuera del rango(1-5)")
            leer_opcion()
        else:
            if(opcion == 1):
                sumar()
            elif(opcion == 2):
                restar()
            elif(opcion == 3):
                multiplicar()
            elif(opcion == 4):
                dividir()   
         
    except:
        print("seleccione una opcion valida")
        leer_opcion()
        return
def leer_numero1():
    try:
        numero1 = float(input("ingrese el primer numero:"))
        return numero1
    except:
        print("Error no ingresaste un numero")
        n2=leer_numero1()
    
def leer_numero2():
    try:
        numero2 = float(input("ingrese el segundo numero:"))
        return numero2
    except:
        print("Error no ingresaste un numero")
        n2=leer_numero2()


def sumar():
    try:
        n1=float(input("Ingrese el primer numero:"))
        n2=float(input("Ingresa el segundo numero:"))
        print("La suma de los numeros es:",n1+n2)
        menu()
    except:
        print("ERROR NO INGRESASTE UN NÚMERO")
        sumar()
def restar():
    try:
        n1=float(input("Ingrese el primer numero:"))
        n2=float(input("Ingresa el segundo numero:"))
        print("La resta de los numeros es:",n1-n2)
        menu()
    except:
        print("ERROR NO INGRESASTE UN NÚMERO")
        restar()
def multiplicar():
    try:
        n1=float(input("Ingrese el primer numero:"))
        n2=float(input("Ingresa el segundo numero:"))
        print("La multiplicación de los numeros es:",n1*n2)
        menu()
    except:
        print("ERROR NO INGRESASTE UN NÚMERO")
        multiplicar()
def dividir():
    try:
        n1=float(input("Ingrese el primer numero:"))
        n2=float(input("Ingresa el segundo numero:"))
        try:
            print("La división de los numeros es:",n1/n2)
            menu()
        except:
            print("La división por 0 es imposible")
            dividir()
    except:
        print("ERROR NO INGRESASTE UN NÚMERO")
        dividir()
menu()


