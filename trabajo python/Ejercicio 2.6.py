#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
#cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

# dos formas de hacerlo
def inversa_automatica(cadena):
    return cadena[::-1]


def inversa_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida

    return cadena_invertida


print(inversa_manual("Estoy probando"))