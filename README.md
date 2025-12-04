SAFEKEY VAULT+
Sistema Integral de Gestión, Generación y Cifrado de Contraseñas
Versión: 1.0
Autor: Omar Torrez
Descripción General
SAFEKEY VAULT+ es un sistema integral diseñado para la gestión profesional de
contraseñas, incorporando:
• Cifrado mediante el algoritmo Cifrado César
• Protección con contraseña maestra
• CRUD completo de contraseñas
• Generador seguro de contraseñas
• Análisis de fuerza basado en expresiones regulares
• Módulo de búsqueda recursiva
• Registro de acciones en archivo log
• Validación robusta de entradas
• Persistencia en archivos .txt
Este sistema está implementado íntegramente en Python, siguiendo buenas prácticas de
modularización, seguridad básica y control de errores.
Estructura del Sistema (Módulos)
El proyecto se compone lógicamente de 8 módulos funcionales:
1 Cifrado y Descifrado
Funciones:
• encriptar_cesar()
• desencriptar_cesar()
Implementa el algoritmo Cifrado César para proteger contraseñas almacenadas.
2 Sistema de Acceso — Contraseña Maestra
Funciones:
• verificar_contrasena()
Permite que solo el usuario autorizado acceda al sistema.
La contraseña maestra se almacena cifrada en contrasena.txt.
3Validación de Datos
Funciones:
• verificar_opciones()
Evita errores críticos validando:
• tipo de dato
• rango
• número de opciones válidas
• excepciones
• valores nulos
4CRUD de Contraseñas (Gestión Completa)
Funciones:
• agregar_contrasena()
• consultar_contrasenas()
• editar_contrasena()
• eliminar_contrasena()
Las contraseñas se almacenan en contrasenas.txt junto con su:
• usuario
• correo
• app/plataforma
• contraseña cifrada
• fecha de creación
5 Analizador de Fuerza de Contraseña
Función:
• analizar_fuerza_contrasena()
Evalúa características como:
✔ longitud
✔ uso de mayúsculas
✔ números
✔ símbolos
✔ patrones débiles (123, password, abc…)
✔ entropía simple
6Generador Seguro de Contraseñas
Función:
• generar_contrasena_segura()
Permite generar contraseñas aleatorias con:
• letras mayúsculas/minúsculas
• números
• símbolos
• longitudes personalizadas
7 Búsqueda Recursiva
Función:
• buscar_texto_recursivo()
Permite localizar coincidencias dentro de campos de texto usando recursión pura.
Este módulo demuestra dominio de técnicas avanzadas en programación.
8Registro (Log) de Acciones
Función:
• registrar_acciones()
Registra eventos como:
• creación
• edición
• eliminación
• intentos de acceso
• consultas
Archivos del Proyecto
Archivo Descripción
main.py Menú principal y flujo del programa
contrasena.txt Contraseña maestra cifrada
contrasenas.txt Base de datos simple de contraseñas cifradas
log.txt Registro histórico de acciones
README.md Este documento
Instalación
1. Instalar Python 3.9+
2. Clonar o descargar el proyecto
3. Ejecutar desde la terminal:
python3 main.py
No requiere librerías externas, solo módulos estándar de Python:
• time
• re
• random
Uso del Programa
1. Iniciar el sistema
Si es la primera ejecución, el programa pedirá configurar una contraseña maestra, la
cual será cifrada.
2. Menú principal
Incluye:
• Agregar contraseña
• Ver contraseñas
• Editar
• Eliminar
• Generar contraseña segura
• Analizar fuerza
• Buscar (recursivo)
• Salir
Seguridad Implementada
• Cifrado básico (César) para almacenamiento
• Acceso controlado
• Archivos separados para credenciales
• Validación robusta con manejo de errores
• Logs para auditoría
• Evita patrones débiles
• Controla caracteres peligrosos (como comas)
Principios Técnicos Usados
• Programación modular
• Recursividad
• Validación de datos
• Persistencia en archivos
• Patrones de diseño simples
• Manejo de excepciones
• Expresiones regulares avanzadas
• Encapsulamiento funcional
• Buenas prácticas de I/O
Futuras Mejoras (Opcionales)
• Implementar cifrado AES real con cryptography
• Migrar la base de datos a SQLite
• Crear versión GUI con Tkinter o PyQt
• Generar exportación en JSON o CSV
• Añadir recuperación de contraseña maestra mediante preguntas de seguridad
Conclusión
SAFEKEY VAULT+ es un sistema completo que combina:
seguridad + recursividad + modularización + análisis de fuerza + generación segura +
control de accesos.
Es un proyecto competente, profesional y totalmente funcional
