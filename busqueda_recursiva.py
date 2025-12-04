def buscar_texto_recursivo(texto_principal, texto_a_buscar):
    if not texto_a_buscar:
        return True
    if len(texto_principal) < len(texto_a_buscar):
        return False
    if texto_principal.startswith(texto_a_buscar):
        return True
    return buscar_texto_recursivo(texto_principal[1:], texto_a_buscar)