import random
numero_aleatorio=random.randint(1,10)
print("Juego de adivinar número secreto")
numero_usuario=0;
while(numero_usuario!=numero_aleatorio):
    numero_usuario=int(input("Ingrese un número: "))
    if(numero_usuario>=0 and numero_usuario<=11):
        if (numero_usuario==numero_aleatorio):
            print(f"Bien hecho, el número secreto era {numero_aleatorio}")
        else:
            print(f"No, {numero_usuario} no es el número secreto ")
    else:
        print(f"El número: {numero_usuario} debe ir entre 1 y 10")