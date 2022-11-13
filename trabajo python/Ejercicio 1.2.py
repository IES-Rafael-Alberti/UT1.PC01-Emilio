#Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que sigue):

num1=int(input("Introduzca numero 1"))
num2=int(input("Introduzca numero 2"))


if num1 > num2:
    print(f"El numero {num1} es mayor")
elif num1==num2:
    print(f"Estos numeros son iguales {num1}")
else:
    print(f"El numero {num2} es mayor")

