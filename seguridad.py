import re

def analizar_fuerza_contrasena(contrasena):
    puntuacion = 0
    longitud = len(contrasena)
    
    if longitud < 8:
        puntuacion += 0
    elif 8 <= longitud < 12:
        puntuacion += 1
    else:
        puntuacion += 2

    if len(re.findall(r"[A-Z]", contrasena)) < 2:
        puntuacion += 0
    elif 2 <= len(re.findall(r"[A-Z]", contrasena)) < 4:
        puntuacion += 1
    else:
        puntuacion += 2

    if len(re.findall(r"\d", contrasena)) < 2:
        puntuacion += 0
    elif 2 <= len(re.findall(r"\d", contrasena)) < 4:
        puntuacion += 1
    else:
        puntuacion += 2

    if len(re.findall(r"[^a-zA-Z0-9\s]", contrasena)) < 1:
        puntuacion += 0
    elif 1 <= len(re.findall(r"[^a-zA-Z0-9\s]", contrasena)) < 3:
        puntuacion += 1
    else:
        puntuacion += 2

    patrones_prohibidos = [
        "password", "123456", "qwerty", "asdfgh", "123", "abc"
    ]
    contrasena_lower = contrasena.lower()
    
    for patron in patrones_prohibidos:
        if patron in contrasena_lower:
            puntuacion -= 2
            break

    if puntuacion <= 0:
        fuerza = "Muy Débil"
    elif 1 <= puntuacion <= 2:
        fuerza = "Débil"
    elif 3 <= puntuacion <= 4:
        fuerza = "Moderada"
    else:
        fuerza = "Fuerte"
    
    return fuerza, puntuacion