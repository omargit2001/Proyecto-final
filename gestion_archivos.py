import time
from datetime import datetime
from cifrado_cesar import encriptar_cesar, desencriptar_cesar

def agregar_contrasena(servicio, usuario, contrasena):
    fecha = time.strftime("%Y-%m-%d")
    while "," in servicio or "," in usuario or "," in contrasena:
        print("No se permiten comas en los campos de servicio, usuario o contraseña.")
        servicio = input("Ingrese el servicio: ")
        usuario = input("Ingrese el usuario: ")
        contrasena = input("Ingrese la contraseña: ")
    
    with open("contrasenas.txt", "a") as archivo:
        archivo.write(f"{servicio},{usuario},{encriptar_cesar(contrasena)},{fecha}\n")

def consultar_contrasenas(desencriptar=False):
    with open("contrasenas.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    print("Servicio | Usuario | Contraseña | fecha ")
    for linea in lineas[1:]:
        datos = linea.strip().split(",")
        if desencriptar:
            print(f"{datos[0]}, {datos[1]}, {desencriptar_cesar(datos[2])}, {datos[3]}")
        else:
            print(f"{datos[0]}, {datos[1]}, {datos[2]}, {datos[3]}")
    
    return lineas

def editar_contrasena(fila, contrasena):
    with open("contrasenas.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    datos = lineas[fila].strip().split(",")
    datos[2] = encriptar_cesar(contrasena)
    lineas[fila] = ",".join(datos) + "\n"
    
    with open("contrasenas.txt", "w") as archivo:
        archivo.writelines(lineas)

def eliminar_contrasena(fila):
    with open("contrasenas.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    lineas.pop(fila)
    
    with open("contrasenas.txt", "w") as archivo:
        archivo.writelines(lineas)

def buscar_contrasena(texto, lineas):
    texto = texto.lower()
    for linea in lineas[1:]:
        datos = linea.strip().split(",")
        from busqueda_recursiva import buscar_texto_recursivo
        if (buscar_texto_recursivo(datos[0].lower(), texto) or 
            buscar_texto_recursivo(datos[1].lower(), texto)):
            print(linea)