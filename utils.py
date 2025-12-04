def verificar_opciones(opcion, opciones_validas, tipo):
    if len(opciones_validas) != 0:
        while not isinstance(opcion, tipo) or opcion not in opciones_validas:
            try:
                opcion = tipo(opcion)
                if opcion not in opciones_validas:
                    raise ValueError
            except ValueError:
                print(f"Valor invalido, Intente nuevamente.")
                opcion = input("Ingrese una opción: ")
    else:
        while not isinstance(opcion, tipo):
            try:
                opcion = tipo(opcion)
                if isinstance(opcion, int) or isinstance(opcion, float):
                    if opcion < 0:
                        raise ValueError
            except ValueError:
                print(f"Valor invalido, Intente nuevamente.")
                opcion = input("Ingrese una opción: ")
    return opcion

def verificar_contrasena(texto):
    try:
        with open("contrasena.txt", "r") as archivo:
            contrasena_encriptada = archivo.read().strip()
        from cifrado_cesar import desencriptar_cesar
        contrasena_desencriptada = desencriptar_cesar(contrasena_encriptada)
        return texto == contrasena_desencriptada
    except FileNotFoundError:
        return False