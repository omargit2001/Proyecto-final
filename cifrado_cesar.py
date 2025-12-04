def encriptar_cesar(texto, desplazamiento=1):
    resultado = ""
    for letra in texto:
        if 'a' <= letra <= 'z':  # Minúsculas
            inicio = ord('a')
            caracter_cifrado = chr((ord(letra) - inicio + desplazamiento) % 26 + inicio)
        elif 'A' <= letra <= 'Z':  # Mayúsculas
            inicio = ord('A')
            caracter_cifrado = chr((ord(letra) - inicio + desplazamiento) % 26 + inicio)
        else:  # Otros caracteres (números, símbolos, espacios) se mantienen sin cambios
            caracter_cifrado = letra
        resultado += caracter_cifrado
    return resultado

def desencriptar_cesar(texto, desplazamiento=1):
    resultado = ""
    for letra in texto:
        if 'a' <= letra <= 'z':  # Minúsculas
            inicio = ord('a')
            caracter_cifrado = chr((ord(letra) - inicio - desplazamiento) % 26 + inicio)
        elif 'A' <= letra <= 'Z':  # Mayúsculas
            inicio = ord('A')
            caracter_cifrado = chr((ord(letra) - inicio - desplazamiento) % 26 + inicio)
        else:  # Otros caracteres (números, símbolos, espacios) se mantienen sin cambios
            caracter_cifrado = letra
        resultado += caracter_cifrado
    return resultado