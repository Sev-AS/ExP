import json
import os

#CRUD en Json - Contactos

#Menu principal
def mostrarMenu():
    menu = """
┌────────────────────────────────────────────────┐
│     ╔═╗╦═╗╦ ╦╔╦╗  ╔═╗╔═╗╔╗╔╔╦╗╔═╗╔═╗╔╦╗╔═╗     │
│     ║  ╠╦╝║ ║ ║║  ║  ║ ║║║║ ║ ╠═╣║   ║ ║ ║     │
│     ╚═╝╩╚═╚═╝═╩╝  ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝ ╩ ╚═╝     │
└────────────────────────────────────────────────┘s
        Create | Read | Update | Delete

╔════════════════════════════════════════════════╗
║                   OPCIONES                     ║
╠════════════════════════════════════════════════╣
║  1. Crear contacto                             ║
║  2. Mostrar todos los contactos                ║
║  3. Buscar contacto por ID                     ║
║  4. Actualizar contacto                        ║
║  5. Eliminar contacto                          ║
║  0. Salir                                      ║
╚════════════════════════════════════════════════╝

Seleccione una opcion: """
    return menu

def limpiarTerminal(mensaje=True):
    if mensaje==True:
        print("\n Presiona enter para continuar...")
        input()
        os.system("clear")
    else:
        os.system("clear")

#Leer archivos JSON
def leerArchivosJSON(path:str):
    try:
        with open(path, mode='r') as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        print(f' Creando archivo {path} por primera vez...')
        return []
    except json.JSONDecodeError:
        print(f' Error: El archivo {path} no tiene un formato JSON valido.')
        return []
    except Exception as e:
        print(f' Error: {e}')
        return []

#Escribir archivos JSON
def escribirArchivosJSON(path:str, datos):
    try:
        with open(path, mode='w') as file:
            json.dump(datos, file)
        return True
    except Exception as e:
        print(f' Error al guardar: {e}')
        return False

#Mostrar contactos en formato tabla
def mostrarContactos(contactos):
    if not contactos:
        print("\n No hay contactos registrados.")
        return
    
    print("\n╔════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                    LISTA DE CONTACTOS                              ║")
    print("╠════╦══════════════════════╦═══════════════════╦════════════════════════════════════╣")
    print("║ ID ║        NOMBRE        ║     TELeFONO      ║              EMAIL                 ║")
    print("╠════╬══════════════════════╬═══════════════════╬════════════════════════════════════╣")
    
    for contacto in contactos:
        nombre = contacto['Nombre'][:20].ljust(20)  # Limitar y rellenar nombre para mantener estetica
        telefono = contacto['Telefono'][:17].ljust(17)  # Limitar y rellenar telefono para mantener estetica
        email = contacto['Email'][:34].ljust(34)  # Limitar y rellenar email para mantener estetica
        
        print(f"║{str(contacto['ID']).center(4)}║ {nombre} ║ {telefono} ║ {email} ║")
    
    print("╚════╩══════════════════════╩═══════════════════╩════════════════════════════════════╝")
    print(f"\n Total de contactos: {len(contactos)}")

#Generar nuevo ID
def generarNuevoID(contactos):
    if not contactos:
        return 1
    return max(contacto['ID'] for contacto in contactos) + 1

#Crear contacto
def crearContacto(contactos):
    print("\n╔═══════════════════════════════════╗")
    print("║           CREAR CONTACTO          ║")
    print("╚═══════════════════════════════════╝")
    
    try:
        # Solicitar datos
        nombre = input("Nombre completo: ")
        if not nombre:
            print(" El nombre no puede estar vacio.")
            return contactos
        
        telefono = input("Telefono: ")
        if not telefono:
            print(" El telefono no puede estar vacio.")
            return contactos
        
        email = input(" Email: ")
        if not email:
            print(" El email no puede estar vacio.")
            return contactos

        
        # Verificar si el email ya existe
        for contacto in contactos:
            if contacto['Email'] == email:
                print(" Ya existe un contacto con este email.")
                return contactos
        
        # Crear nuevo contacto
        nuevo_contacto = {
            "ID": generarNuevoID(contactos),
            "Nombre": nombre,
            "Telefono": telefono,
            "Email": email
        }
        
        contactos.append(nuevo_contacto)
        print(f"\nContacto creado exitosamente con ID: {nuevo_contacto['ID']}")
        
    except Exception as e:
        print(f" Error al crear contacto: {e}")
    
    return contactos

#Buscar contacto por ID
def buscarContactoPorID(contactos):
    print("\n╔═══════════════════════════════════╗")
    print("║          BUSCAR CONTACTO          ║")
    print("╚═══════════════════════════════════╝")
    
    try:
        id_buscar = int(input("Ingrese el ID del contacto: "))
        
        for contacto in contactos:
            if contacto['ID'] == id_buscar:
                print("\n╔═══════════════════════════════════════════════════════════════╗")
                print("║                        CONTACTO ENCONTRADO                    ║")
                print("╠═══════════════════════════════════════════════════════════════╣")
                print(f"║ ID:       {str(contacto['ID']).ljust(49)} ║")#Mantener estetica "ljust"
                print(f"║ Nombre:   {contacto['Nombre'].ljust(49)} ║")
                print(f"║ Telefono: {contacto['Telefono'].ljust(49)} ║")
                print(f"║ Email:    {contacto['Email'].ljust(49)} ║")
                print("╚═══════════════════════════════════════════════════════════════╝")
                return
        
        print(f" No se encontro ningun contacto con ID: {id_buscar}")
        
    except ValueError:
        print(" El ID debe ser un numero valido.")
    except Exception as e:
        print(f" Error: {e}")

#Actualizar contacto
def actualizarContacto(contactos):
    print("\n╔═══════════════════════════════════╗")
    print("║      ACTUALIZAR CONTACTO          ║")
    print("╚═══════════════════════════════════╝")
    
    try:
        id_actualizar = int(input("Ingrese el ID del contacto a actualizar: "))
        
        contacto_encontrado = None
        for contacto in contactos:
            if contacto['ID'] == id_actualizar:
                contacto_encontrado = contacto
                break
        
        if not contacto_encontrado:
            print(f" No se encontro ningun contacto con ID: {id_actualizar}")
            return contactos
        
        print(f"\nContacto actual:")
        print(f"   Nombre: {contacto_encontrado['Nombre']}")
        print(f"   Telefono: {contacto_encontrado['Telefono']}")
        print(f"   Email: {contacto_encontrado['Email']}")
        
        print("\n💡 Presione Enter para mantener el valor actual")
        
        # Actualizar nombre
        nuevo_nombre = input(f"👤 Nuevo nombre [{contacto_encontrado['Nombre']}]: ")
        if nuevo_nombre:
            contacto_encontrado['Nombre'] = nuevo_nombre
        
        # Actualizar telefono
        nuevo_telefono = input(f"📞 Nuevo telefono [{contacto_encontrado['Telefono']}]: ")
        if nuevo_telefono:
            contacto_encontrado['Telefono'] = nuevo_telefono
        
        # Actualizar email
        nuevo_email = input(f" Nuevo email [{contacto_encontrado['Email']}]: ")
        if nuevo_email:    
            # Verificar si el nuevo email ya existe en otro contacto
            email_existe = False
            for contacto in contactos:
                if contacto['ID'] != id_actualizar and contacto['Email'] == nuevo_email:
                    email_existe = True
                    break
            if email_existe:
                print(" Ya existe otro contacto con este email. Manteniendo email actual.")
            else:
                contacto_encontrado['Email'] = nuevo_email
        
        print(f"\nContacto con ID {id_actualizar} actualizado exitosamente.")
        
    except ValueError:
        print(" El ID debe ser un numero valido.")
    except Exception as e:
        print(f" Error: {e}")
    
    return contactos

#Eliminar contacto
def eliminarContacto(contactos):
    print("\n╔═══════════════════════════════════╗")
    print("║        ELIMINAR CONTACTO          ║")
    print("╚═══════════════════════════════════╝")
    
    try:
        id_eliminar = int(input("Ingrese el ID del contacto a eliminar: "))
        
        contacto_encontrado = None
        indice_contacto = -1
        
        for i, contacto in enumerate(contactos):
            if contacto['ID'] == id_eliminar:
                contacto_encontrado = contacto
                indice_contacto = i
                break
        
        if not contacto_encontrado:
            print(f" No se encontro ningun contacto con ID: {id_eliminar}")
            return contactos
        
        print(f"\n ¿Esta seguro de eliminar este contacto?")
        print(f"   Nombre: {contacto_encontrado['Nombre']}")
        print(f"   Telefono: {contacto_encontrado['Telefono']}")
        print(f"   Email: {contacto_encontrado['Email']}")
        
        confirmacion = input("\nEscriba 'SI' para confirmar: ").upper()
        
        if confirmacion == 'SI':
            contactos.pop(indice_contacto)
            print(f"\nContacto con ID {id_eliminar} eliminado exitosamente.")
        else:
            print("\n Eliminacion cancelada.")
        
    except ValueError:
        print(" El ID debe ser un numero valido.")
    except Exception as e:
        print(f" Error: {e}")
    
    return contactos

# Funcion principal
def main():
    archivo_contactos = 'contacts.json'
    
    while True:
        limpiarTerminal(False)
        print(mostrarMenu())
        
        try:
            opcion = input()
            limpiarTerminal(False)
            
            # Cargar contactos
            contactos = leerArchivosJSON(archivo_contactos)
            
            if opcion == '1':
                contactos = crearContacto(contactos)
                if escribirArchivosJSON(archivo_contactos, contactos):
                    print(" Contacto guardado exitosamente.")
                
            elif opcion == '2':
                mostrarContactos(contactos)
                
            elif opcion == '3':
                buscarContactoPorID(contactos)
                
            elif opcion == '4':
                contactos = actualizarContacto(contactos)
                if escribirArchivosJSON(archivo_contactos, contactos):
                    print(" Cambios guardados exitosamente.")
                
            elif opcion == '5':
                contactos = eliminarContacto(contactos)
                if escribirArchivosJSON(archivo_contactos, contactos):
                    print(" Cambios guardados exitosamente.")

            elif opcion == '0':
                print("¡Gracias por usar el gestor de contactos!")
                break
                
            else:
                print(" Opcion no valida. Intente nuevamente.")
            
            if opcion != '0':
                limpiarTerminal()

        except Exception as e:
            print(f" Error inesperado: {e}")
            limpiarTerminal()
#Ejecutar main

main()