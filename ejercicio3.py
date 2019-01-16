#creacion de una función
def saludo():
    nombre = input("ingrese su nombre:")
    apellido = input("ingrese su apellido:")
    sexo = input("ingrese su sexo(masculino o femenino):")

    if(sexo == "masculino"):
        print("Hola Sr.",nombre,apellido)
    elif(sexo == "femenino"):
        print("Hola Sra.",nombre,apellido)
    else:
        print("error el sexo debe ser masculino o femenino!!")
        saludo()

saludo()