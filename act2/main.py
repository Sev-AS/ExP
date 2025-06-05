import csv
import json
import os

#Limpiar terminal
def limpiarTerminal(mensaje=True):
    if mensaje==True:
        print("\n Presiona enter para limpiar...")
        input()
        os.system("clear")
    else:
        os.system("clear")

#Leer archivos TXT
def leerArchivosTXT(path:str) -> list:
    try:
        with open(path, mode='r') as file:
            for row, linea in enumerate(file, start=1):
                print(f"{row}. {linea.strip()}")
    except FileNotFoundError:
        print(f'Error: El archivo {path} no existe.')
    except Exception as e:
        print(f'Error: {e}')

#Escribir archivos TXT
def escribirArchivosTXT(path:str, lineas:list):
    try:
        with open(path, mode='a') as file:
            file.writelines(lineas)
        print(f"Contenido añadido correctamente a {path}")
    except Exception as e:
        print(f'Error: {e}')

#Sobrescribir archivos TXT
def sobrescribirArchivosTXT(path:str, contenido:str):
    try:
        with open(path, mode='w') as file:
            file.write(contenido)
        print(f"Archivo {path} sobrescrito correctamente")
    except Exception as e:
        print(f'Error: {e}')

#Leer archivos CSV
def leerArchivosCSV(path:str) -> list:
    try:
        with open(path, mode='r') as file:
            reader = csv.DictReader(file)
            lineas = list(reader)
            for row in lineas:
                print(f"ID: {row['id']} - Nombre: {row['nombre'].strip()} - Ciudad: {row['ciudad'].strip()}")
            return lineas
    except FileNotFoundError:
        print(f'Error: El archivo {path} no existe.')
        return []
    except Exception as e:
        print(f'Error: {e}')
        return []

#Escribir archivos CSV
def escribirArchivosCSV(path:str, datos:list, campos:list):
    try:
        with open(path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            writer.writerows(datos)
        print(f"Archivo CSV {path} creado correctamente")
    except Exception as e:
        print(f'Error: {e}')

#Filtrar usuarios por ciudad
def filtrarUsuariosPorCiudad(path:str, ciudad:str):
    try:
        with open(path, mode='r') as file:
            reader = csv.DictReader(file)
            usuarios_filtrados = []
            for row in reader:
                if row['ciudad'].strip().lower() == ciudad.lower():
                    usuarios_filtrados.append(row)
                    print(f"ID: {row['id']} - Nombre: {row['nombre'].strip()} - Ciudad: {row['ciudad'].strip()}")
            
            if not usuarios_filtrados:
                print(f"No se encontraron usuarios en {ciudad}")
            return usuarios_filtrados
    except FileNotFoundError:
        print(f'Error: El archivo {path} no existe.')
        return []
    except Exception as e:
        print(f'Error: {e}')
        return []

#Actualizar ciudad de usuario
def actualizarCiudadUsuario(path:str, user_id:int, nueva_ciudad:str):
    try:
        # Leer datos actuales
        usuarios = []
        with open(path, mode='r') as file:
            reader = csv.DictReader(file)
            usuarios = list(reader)
        
        # Actualizar usuario
        usuario_encontrado = False
        for usuario in usuarios:
            if int(usuario['id']) == user_id:
                usuario['ciudad'] = nueva_ciudad
                usuario_encontrado = True
                print(f"Usuario {usuario['nombre'].strip()} actualizado a ciudad: {nueva_ciudad}")
                break
        
        if not usuario_encontrado:
            print(f"No se encontró usuario con ID: {user_id}")
            return
        
        # Sobrescribir archivo
        with open(path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'ciudad'])
            writer.writeheader()
            writer.writerows(usuarios)
        
        print(f"Archivo {path} actualizado correctamente")
        
    except FileNotFoundError:
        print(f'Error: El archivo {path} no existe.')
    except Exception as e:
        print(f'Error: {e}')

#Leer archivos JSON
def leerArchivosJSON(path:str):
    try:
        with open(path, mode='r') as file:
            datos = json.load(file)
            print(f"Contenido de {path}:")
            print(json.dumps(datos, indent=2, ensure_ascii=False))
            return datos
    except FileNotFoundError:
        print(f'Error: El archivo {path} no existe.')
        return None
    except json.JSONDecodeError:
        print(f'Error: El archivo {path} no tiene un formato JSON válido.')
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None

#Escribir archivos JSON
def escribirArchivosJSON(path:str, datos):
    try:
        with open(path, mode='w') as file:
            json.dump(datos, file, indent=2, ensure_ascii=False)
        print(f"Archivo JSON {path} creado correctamente")
    except Exception as e:
        print(f'Error: {e}')

#Convertir CSV a JSON
def convertirCSVaJSON(csv_path:str, json_path:str):
    try:
        # Leer CSV
        with open(csv_path, mode='r', ng='utf-8') as file:
            reader = csv.DictReader(file)
            datos = []
            for row in reader:
                # Limpiar espacios en blanco
                row_limpio = {k: v.strip() if isinstance(v, str) else v for k, v in row.items()}
                datos.append(row_limpio)
        
        # Escribir JSON
        with open(json_path, mode='w', ng='utf-8') as file:
            json.dump(datos, file, indent=2, ensure_ascii=False)
        
        print(f"Conversión exitosa: {csv_path} -> {json_path}")
        
    except FileNotFoundError:
        print(f'Error: El archivo {csv_path} no existe.')
    except json.JSONDecodeError:
        print(f'Error: Problema al crear el archivo JSON.')
    except Exception as e:
        print(f'Error: {e}')

#Manejo de excepciones str + int
def manejarConcatenacion():
    while True:
        try:
            nombre = input("Ingrese su nombre: ")
            edad_str = input("Ingrese su edad: ")
            edad = int(edad_str)
            
            mensaje = "La edad de " + nombre + " es " + str(edad)
            print(mensaje)
            break
            
        except ValueError:
            print("Error: La edad debe ser un número válido. Intente nuevamente.")
        except Exception as e:
            print(f'Error inesperado: {e}')

#Crear archivos iniciales
def crearArchivosEjemplo():
    # Crear usuarios.csv con más usuarios
    usuarios = [
        {"id": 1, "nombre": "Carlos", "ciudad": "Bogotá"},
        {"id": 2, "nombre": "Maria", "ciudad": "Cali"},
        {"id": 3, "nombre": "Juan", "ciudad": "Bogotá"},
        {"id": 4, "nombre": "Ana", "ciudad": "Medellín"},
        {"id": 5, "nombre": "Pedro", "ciudad": "Bogotá"}
    ]
    escribirArchivosCSV('usuarios.csv', usuarios, ['id', 'nombre', 'ciudad'])
    
    # Crear productos.json
    productos = [
        {"id": 1, "nombre": "Laptop", "precio": 1500.99},
        {"id": 2, "nombre": "Mouse", "precio": 25.50},
        {"id": 3, "nombre": "Teclado", "precio": 45.00}
    ]
    escribirArchivosJSON('productos.json', productos)

#Menu basico
menu = """
==============================================================
    EJERCICIOS PRÁCTICOS DE MANEJO DE ARCHIVOS
==============================================================
1. Leer y mostrar un archivo de texto línea a línea
2. Sobrescribir un archivo de texto y luego añadir contenido
3. Leer y mostrar un archivo csv línea a línea
4. Actualizar un CSV (lectura-escritura)
5. Leer y escribir JSON de productos
6. Convertir CSV a JSON
7. Manejo de excepciones en concatenación de (str + int)
8. Crear archivos de ejemplo
9. Filtrar usuarios por ciudad (Bogotá)
0. Salir
==============================================================
Seleccione una opción para ejecutar el ejercicio correspondiente: 
    """

#Logica/Menu  
while True:
    print(menu)
    opcion = input().strip()
    limpiarTerminal(False)
    
    if opcion == "1":
        print("=== Ejercicio 1: Leer archivo de texto ===")
        leerArchivosTXT('notas.txt')
        limpiarTerminal()
        
    elif opcion == "2":
        print("=== Ejercicio 2: Sobrescribir y añadir contenido ===")
        # Sobrescribir diario.txt
        sobrescribirArchivosTXT('diario.txt', 'Fecha: 2025-06-02\n')
        
        # Añadir actividades
        actividad1 = input("Ingrese la primera actividad del día: ")
        actividad2 = input("Ingrese la segunda actividad del día: ")
        escribirArchivosTXT('diario.txt', [actividad1 + '\n', actividad2 + '\n'])
        
        # Mostrar contenido completo
        print("\nContenido completo del diario:")
        leerArchivosTXT('diario.txt')
        limpiarTerminal()
        
    elif opcion == "3":
        print("=== Ejercicio 3: Leer archivo CSV ===")
        leerArchivosCSV('usuarios.csv')
        limpiarTerminal()
        
    elif opcion == "4":
        print("=== Ejercicio 4: Actualizar CSV ===")
        print("Usuarios actuales:")
        leerArchivosCSV('usuarios.csv')
        try:
            user_id = int(input("\nIngrese el ID del usuario a actualizar: "))
            nueva_ciudad = input("Ingrese la nueva ciudad: ")
            actualizarCiudadUsuario('usuarios.csv', user_id, nueva_ciudad)
        except ValueError:
            print("Error: El ID debe ser un número válido.")
        limpiarTerminal()
        
    elif opcion == "5":
        print("=== Ejercicio 5: Manejo de JSON ===")
        # Leer productos existentes
        productos = leerArchivosJSON('productos.json')
        
        if productos is not None:
            # Añadir nuevo producto
            try:
                nuevo_id = int(input("\nIngrese ID del nuevo producto: "))
                nuevo_nombre = input("Ingrese nombre del producto: ")
                nuevo_precio = float(input("Ingrese precio del producto: "))
                
                nuevo_producto = {"id": nuevo_id, "nombre": nuevo_nombre, "precio": nuevo_precio}
                productos.append(nuevo_producto)
                
                escribirArchivosJSON('productos.json', productos)
                print("\nProductos actualizados:")
                leerArchivosJSON('productos.json')
                
            except ValueError:
                print("Error: ID debe ser entero y precio debe ser decimal.")
        limpiarTerminal()
        
    elif opcion == "6":
        print("=== Ejercicio 6: Convertir CSV a JSON ===")
        convertirCSVaJSON('usuarios.csv', 'usuarios.json')
        print("\nContenido del JSON generado:")
        leerArchivosJSON('usuarios.json')
        limpiarTerminal()
        
    elif opcion == "7":
        print("=== Ejercicio 7: Manejo de excepciones ===")
        manejarConcatenacion()
        limpiarTerminal()
        
    elif opcion == "8":
        print("=== Crear archivos de ejemplo ===")
        crearArchivosEjemplo()
        print("Archivos de ejemplo creados correctamente.")
        limpiarTerminal()
        
    elif opcion == "9":
        print("=== Filtrar usuarios por ciudad (Bogotá) ===")
        filtrarUsuariosPorCiudad('usuarios.csv', 'Bogotá')
        limpiarTerminal()
        
    elif opcion == "0":
        print("¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Intente nuevamente.")
        limpiarTerminal(False)