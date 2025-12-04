from random import randint

def generar_contrasena_segura(longitud, mayusculas=True, numeros=True, simbolos=True):
    Minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Simbolos = ["-", ".", "+", "_", "?", "!", ":", ";", "'", "¡", "¿"]
    
    caracteres = Minusculas.copy()
    if mayusculas:
        caracteres += Mayusculas
    if numeros:
        caracteres += Numeros
    if simbolos:
        caracteres += Simbolos
    
    contrasena = ""
    for i in range(longitud):
        numero_aleatorio = randint(0, len(caracteres)-1)
        contrasena += caracteres[numero_aleatorio]
    
    return contrasena