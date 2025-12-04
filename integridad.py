from datetime import datetime
from auditoria import revisar_integridad_recursiva, registrar_acciones
from cifrado_cesar import encriptar_cesar, desencriptar_cesar

def verificar_vault_integridad():
    print("\nIniciando revisión de integridad de SafeKey Vault+...")
    
    try:
        with open("contrasenas.txt", "r") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        registrar_acciones("Error de Integridad", "Archivo 'contrasenas.txt' no encontrado.")
        print("El archivo 'contrasenas.txt' no se encontró. No hay contraseñas para verificar.")
        return 0, 0, []
    
    if not lineas:
        registrar_acciones("Revisión Integridad", "Archivo 'contrasenas.txt' está vacío.")
        print("El archivo 'contrasenas.txt' está vacío.")
        return 0, 0, []
    
    titulos = lineas[0].strip()
    lineas_datos = lineas[1:]
    lineas_validas_inicial = []
    conteo_reparos_inicial = 0
    
    lineas_validas_filtradas, conteo_reparos_final = revisar_integridad_recursiva(
        lineas_datos, 0, lineas_validas_inicial, conteo_reparos_inicial
    )
    
    mapa_de_entradas_unicas = {}
    conteo_duplicados = 0
    
    for linea_valida in lineas_validas_filtradas:
        try:
            parts = linea_valida.split(',')
            if len(parts) == 4:
                servicio, usuario, _, fecha_str = parts
                current_date = datetime.strptime(fecha_str, "%Y-%m-%d")
                key = (servicio.lower(), usuario.lower())
                
                if key not in mapa_de_entradas_unicas or current_date > mapa_de_entradas_unicas[key][0]:
                    if key in mapa_de_entradas_unicas:
                        conteo_duplicados += 1
                        registrar_acciones("Revisión Integridad", 
                                         f"Duplicado de servicio/usuario encontrado para '{servicio}'/'{usuario}'. Se mantuvo la entrada más reciente.")
                    mapa_de_entradas_unicas[key] = (current_date, linea_valida)
                else:
                    conteo_duplicados += 1
                    registrar_acciones("Revisión Integridad", 
                                     f"Duplicado de servicio/usuario encontrado para '{servicio}'/'{usuario}'. Se ignoró la entrada más antigua.")
            else:
                conteo_reparos_final += 1
                registrar_acciones("Revisión Integridad", 
                                 f"Formato de línea inesperado durante la verificación de duplicados: '{linea_valida[:50]}'...")
        except ValueError as e:
            conteo_reparos_final += 1
            registrar_acciones("Revisión Integridad", 
                             f"Error al procesar línea para duplicados (fecha o formato inválido): '{linea_valida[:50]}...' Error: {e}")
    
    entradas_unicas_final = [tupla_entrada[1] for tupla_entrada in mapa_de_entradas_unicas.values()]
    
    print("\n--- Informe de Integridad de SafeKey Vault+ ---")
    print(f"Total de registros de contraseñas procesados (excluyendo cabecera): {len(lineas_datos)}")
    print(f"Registros válidos: {len(entradas_unicas_final)}")
    print(f"Registros con problemas (ignorados/reparados): {conteo_reparos_final}")
    print(f"Registros duplicados eliminados: {conteo_duplicados}")
    
    if conteo_reparos_final > 0 or conteo_duplicados > 0:
        print("Consulte 'audit_log.txt' para detalles sobre los registros reparados/ignorados y duplicados.")
    
    total_problemas = conteo_reparos_final + conteo_duplicados
    if total_problemas > 0:
        print("Reescribiendo 'contrasenas.txt' con solo registros válidos y únicos.")
        with open("contrasenas.txt", "w") as f:
            f.write(titulos + "\n")
            for entry in entradas_unicas_final:
                f.write(entry + "\n")
        registrar_acciones("Revisión Integridad", 
                        f"Archivo 'contrasenas.txt' reescrito. {total_problemas} registros con problemas o duplicados removidos.")
    else:
        print("No se encontraron problemas de integridad ni duplicados. El archivo 'contrasenas.txt' está intacto.")
    
    print("-------------------------------------------------")
    return conteo_reparos_final, len(entradas_unicas_final), entradas_unicas_final