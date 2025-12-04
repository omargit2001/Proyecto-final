import time

def registrar_acciones(accion, detalles=""):
    fecha = time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open("audit_log.txt", "a") as archivo:
        archivo.write(f"{fecha} {accion}: {detalles}\n")

def revisar_integridad_recursiva(lineas, index, lineas_validas, conteo_reparos):
    if index >= len(lineas):
        return lineas_validas, conteo_reparos
    
    linea = lineas[index]
    lineastrip = linea.strip()
    problema_hallado = False
    descripcion = ""
    servicio = "desconocido"
    
    if not lineastrip:
        problema_hallado = True
        descripcion = "Registro vacío encontrado y omitido."
    else:
        parts = lineastrip.split(',')
        if len(parts) != 4:
            problema_hallado = True
            descripcion = "Entrada incompleta o formato no reconocido (número de campos incorrecto)."
        else:
            servicio, usuario, contrasena, fecha = parts
            from cifrado_cesar import desencriptar_cesar
            
            patrones_prohibidos = ["password", "123456", "qwerty", "asdfgh", "123", "abc"]
            tiene_patron_prohibido = False
            
            try:
                contrasena_minusculas = desencriptar_cesar(contrasena).lower()
            except:
                contrasena_minusculas = contrasena.lower()
            
            for pattern in patrones_prohibidos:
                if pattern in contrasena_minusculas:
                    tiene_patron_prohibido = True
                    break
            
            if (' ' in contrasena or 
                desencriptar_cesar(desencriptar_cesar(contrasena)) != contrasena or 
                tiene_patron_prohibido):
                problema_hallado = True
                descripcion = f"Contraseña sospechosa/no cifrada para el servicio '{servicio}'."
            
            if not servicio or not usuario or not contrasena or not fecha:
                problema_hallado = True
                descripcion = f"Entrada con campos vacíos para el servicio '{servicio}'."
    
    if problema_hallado:
        conteo_reparos += 1
        detalles_log = descripcion
        if servicio != "desconocido":
            detalles_log = f"Servicio: '{servicio}', {descripcion}"
        registrar_acciones("Revisión Integridad", detalles_log)
    else:
        lineas_validas.append(lineastrip)
    
    return revisar_integridad_recursiva(lineas, index + 1, lineas_validas, conteo_reparos)