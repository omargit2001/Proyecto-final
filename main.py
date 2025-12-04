import time
from IPython.display import clear_output
from cifrado_cesar import encriptar_cesar, desencriptar_cesar
from seguridad import analizar_fuerza_contrasena
from generador_contrasenas import generar_contrasena_segura
from busqueda_recursiva import buscar_texto_recursivo
from gestion_archivos import (agregar_contrasena, consultar_contrasenas, 
                            editar_contrasena, eliminar_contrasena, buscar_contrasena)
from auditoria import registrar_acciones
from integridad import verificar_vault_integridad
from utils import verificar_opciones, verificar_contrasena

# Configuración inicial
def configurar_clave_maestra():
    password = input("Ingrese la contraseña: ")
    password_segura = encriptar_cesar(password)
    with open("contrasena.txt", "w") as file:
        file.write(password_segura)
    print("Contraseña guardada en 'contrasena.txt'")

def inicializar_archivos():
    with open("contrasenas.txt", "w") as archivo:
        archivo.write("servicio,usuario,contrasena,fecha\n")

# Función principal del programa
def main():
    # Verificar si existe archivo de contraseña maestra
    try:
        with open("contrasena.txt", "r") as archivo:
            clave_maestra = archivo.readline().strip()
    except FileNotFoundError:
        print("Primera ejecución. Configure su clave maestra.")
        configurar_clave_maestra()
        inicializar_archivos()
    
    # Autenticación
    contador = 0
    while True:
        contador += 1
        clave = input("Introduzca la clave del SafeKey Vault+: ")
        if verificar_contrasena(clave):
            clear_output(wait=True)
            print("Clave correcta")
            registrar_acciones("Inicio de Sesión", "Clave correcta")
            break
        else:
            clear_output(wait=True)
            print("Clave incorrecta")
            registrar_acciones("Inicio de Sesión", "Clave incorrecta")
            print("Intentos restantes:", 3-contador)
            if contador == 3:
                print("Se han agotado los intentos. El programa se cerrará.")
                return
    
    # Menú principal
    while True:
        print("-------------------------------")
        print("--------SAFEKEY VAULT+--------")
        print("----------------------------------------")
        print("1.- Agregar Contraseña")
        print("2.- Consultar Contraseñas")
        print("3.- Generar Contraseña segura")
        print("4.- Buscar Contraseñas")
        print("5.- Revisar Integridad")
        print("6.- Salir")
        print("----------------------------------------")
        
        opcion = input("Ingrese una opción: ")
        opcion = verificar_opciones(opcion, [1, 2, 3, 4, 5, 6], int)
        
        if opcion == 1:
            clear_output()
            servicio = input("Ingrese el servicio: ")
            usuario = input("Ingrese el usuario: ")
            generar = input("Generar contraseña? (s/n): ")
            generar = verificar_opciones(generar, ["s", "n", "S", "N"], str)
            
            if generar.lower() == "s":
                longitud = input("Ingrese la longitud de la contraseña: ")
                longitud = verificar_opciones(longitud, [], int)
                
                mayusculas = input("Incluir Mayúsculas? (s/n): ")
                mayusculas = verificar_opciones(mayusculas, ["s", "n", "S", "N"], str)
                mayusculas = mayusculas.lower() == "s"
                
                numeros = input("Incluir Numeros? (s/n): ")
                numeros = verificar_opciones(numeros, ["s", "n", "S", "N"], str)
                numeros = numeros.lower() == "s"
                
                simbolos = input("Incluir Simbolos? (s/n): ")
                simbolos = verificar_opciones(simbolos, ["s", "n", "S", "N"], str)
                simbolos = simbolos.lower() == "s"
                
                print("-------------------------------")
                contrasena = generar_contrasena_segura(longitud, mayusculas, numeros, simbolos)
                print(f"Contraseña generada: {contrasena}")
                registrar_acciones("Generada contraseña", f"para '{servicio}'")
            else:
                contrasena = input("Ingrese la contraseña: ")
            
            agregar_contrasena(servicio, usuario, contrasena)
            registrar_acciones("Añadida contraseña", f"para '{servicio}'")
            fuerza, puntaje = analizar_fuerza_contrasena(contrasena)
            print(f"La contraseña es {fuerza} con un puntaje de {puntaje}.")
        
        elif opcion == 2:
            clear_output()
            desencriptar = input("Mostrar Contraseñas desencriptadas? (s/n): ")
            desencriptar = verificar_opciones(desencriptar, ["s", "n", "S", "N"], str)
            print("-------------------------------")
            registrar_acciones("Consultado contraseñas", f"desencriptar {desencriptar}")
            
            lineas = consultar_contrasenas()
            
            print("1.- Editar contraseña")
            print("2.- Eliminar contraseña")
            print("3.- Salir")
            opcion_menu = input("Ingrese una opción: ")
            opcion_menu = verificar_opciones(opcion_menu, [1, 2, 3], int)
            
            if opcion_menu == 1:
                clear_output()
                print("Servicio | Usuario | Contraseña | fecha ")
                i = 0
                for linea in lineas[1:]:
                    i += 1
                    datos = linea.strip().split(",")
                    print(f"{i}. {datos[0]}, {datos[1]}, {datos[2]}, {datos[3]}")
                
                fila = input("Ingrese el número de la contraseña a editar: ")
                fila = verificar_opciones(fila, range(1, i+1), int)
                nueva_contrasena = input("Ingrese la nueva contraseña: ")
                editar_contrasena(fila, nueva_contrasena)
                registrar_acciones("Modificada contraseña", f"para '{datos[0]}'")
            
            elif opcion_menu == 2:
                clear_output()
                print("Servicio | Usuario | Contraseña | fecha ")
                i = 0
                for linea in lineas[1:]:
                    i += 1
                    datos = linea.strip().split(",")
                    print(f"{i}. {datos[0]}, {datos[1]}, {datos[2]}, {datos[3]}")
                
                fila = input("Ingrese el número de la contraseña a eliminar: ")
                fila = verificar_opciones(fila, range(1, i+1), int)
                nombre_servicio = lineas[fila].strip().split(",")[0]
                eliminar_contrasena(fila)
                registrar_acciones("Eliminada contraseña", f"para '{nombre_servicio}'")
        
        elif opcion == 3:
            clear_output()
            longitud = input("Ingrese la longitud de la contraseña: ")
            longitud = verificar_opciones(longitud, [], int)
            
            mayusculas = input("Incluir Mayúsculas? (s/n): ")
            mayusculas = verificar_opciones(mayusculas, ["s", "n", "S", "N"], str)
            mayusculas = mayusculas.lower() == "s"
            
            numeros = input("Incluir Numeros? (s/n): ")
            numeros = verificar_opciones(numeros, ["s", "n", "S", "N"], str)
            numeros = numeros.lower() == "s"
            
            simbolos = input("Incluir Simbolos? (s/n): ")
            simbolos = verificar_opciones(simbolos, ["s", "n", "S", "N"], str)
            simbolos = simbolos.lower() == "s"
            
            print("-------------------------------")
            contrasena_segura = generar_contrasena_segura(longitud, mayusculas, numeros, simbolos)
            registrar_acciones("Generada contraseña segura", 
                            f"longitud {longitud}, mayusculas {mayusculas}, numeros {numeros}, simbolos {simbolos}")
            print(f"Contraseña segura generada: {contrasena_segura}")
            print("-------------------------------")
            fuerza, puntaje = analizar_fuerza_contrasena(contrasena_segura)
            print(f"La contraseña es {fuerza} con un puntaje de {puntaje}.")
            print("-------------------------------")
        
        elif opcion == 4:
            clear_output()
            print("Buscador de Contraseñas\n")
            print("-------------------------------")
            
            with open("contrasenas.txt", "r") as archivo:
                lineas = archivo.readlines()
            
            i = 0
            for linea in lineas[1:]:
                i += 1
                print(f"{i}. {linea}")
            
            while True:
                print("1.- Buscar Contrasena")
                print("2.- Salir")
                opcion_busqueda = input("Ingrese una opción: ")
                print("-------------------------------")
                opcion_busqueda = verificar_opciones(opcion_busqueda, [1, 2], int)
                
                if opcion_busqueda == 1:
                    texto = input("Ingrese el texto a buscar: ")
                    print("-------------------------------")
                    buscar_contrasena(texto, lineas)
                    registrar_acciones("Buscada contraseña", f"para '{texto}'")
                elif opcion_busqueda == 2:
                    break
        
        elif opcion == 5:
            clear_output()
            print("Revisando integridad de SafeKey Vault+")
            print("-------------------------------")
            conteo_reparos, lineas_validas, lineas_datos = verificar_vault_integridad()
        
        elif opcion == 6:
            print("Gracias por usar el programa. ¡Hasta luego!")
            registrar_acciones("Cierre de Sesión", "Programa finalizado")
            return

if __name__ == "__main__":
    main()