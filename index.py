import os

# Definición de arrays para almacenar usuarios y roles
usuarios = []
roles = ["admin", "usuario"]
archivo_usuarios = "usuarios.txt"

# Función para cargar usuarios desde el archivo de texto
def cargar_usuarios_desde_archivo():
    if not os.path.exists(archivo_usuarios):
        return

    with open(archivo_usuarios, "r") as file:
        for line in file:
            datos = line.strip().split(",")
            usuario = {
                "nombre": datos[0],
                "apellido": datos[1],
                "rol": datos[2],
                "correo": datos[3],
                "contraseña": datos[4]
            }
            usuarios.append(usuario)

# Función para guardar usuarios en el archivo de texto
def guardar_usuarios_en_archivo():
    with open(archivo_usuarios, "w") as file:
        for usuario in usuarios:
            datos = [usuario["nombre"], usuario["apellido"], usuario["rol"], usuario["correo"], usuario["contraseña"]]
            file.write(",".join(datos) + "\n")

# Función para registrar un nuevo usuario
def registrar_usuario():
    print("Registro de nuevo usuario")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    print("Roles disponibles: ", roles)
    rol = input("Rol (admin/usuario): ").lower()
    while rol not in roles:
        print("Rol no válido. Intenta nuevamente.")
        rol = input("Rol (admin/usuario): ").lower()
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")

    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "rol": rol,
        "correo": correo,
        "contraseña": contraseña  # Almacenar temporalmente sin encriptar
    }
    usuarios.append(usuario)
    guardar_usuarios_en_archivo()
    print("Usuario registrado con éxito.\n")

# Función para realizar el inicio de sesión
def login():
    print("Inicio de sesión")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")

    for usuario in usuarios:
        if usuario["correo"] == correo and usuario["contraseña"] == contraseña:
            print(f"Bienvenido, {usuario['nombre']} {usuario['apellido']} ({usuario['rol']})")
            return
    print("Correo o contraseña incorrectos. Inténtalo nuevamente.\n")

# Función para listar usuarios (solo el rol "admin" tiene acceso)
def listar_usuarios():
    if es_admin():
        if usuarios:
            print("Listado de usuarios:")
            for usuario in usuarios:
                print(f"{usuario['nombre']} {usuario['apellido']} - {usuario['rol']} - {usuario['correo']}")
            print()
        else:
            print("No hay usuarios registrados.\n")
    else:
        print("Acceso restringido. Solo el rol 'admin' puede listar usuarios.\n")

# Función para listar roles
def listar_roles():
    print("Listado de roles:")
    for rol in roles:
        print(rol)
    print()

# Función para ordenar usuarios por nombre ascendente o descendente
def ordenar_usuarios():
    orden = input("Ordenar usuarios por nombre ascendente (a) o descendente (d): ").lower()
    while orden not in ['a', 'd']:
        print("Opción no válida. Intenta nuevamente.")
        orden = input("Ordenar usuarios por nombre ascendente (a) o descendente (d): ").lower()

    usuarios.sort(key=lambda usuario: usuario['nombre'], reverse=orden == 'd')
    print("Usuarios ordenados:\n")
    listar_usuarios()
    guardar_usuarios_en_archivo()

# Función para verificar si el usuario tiene el rol "admin"
def es_admin():
    return any(usuario["rol"] == "admin" for usuario in usuarios)

# Función para ejecutar el menú principal
def menu_principal():
    cargar_usuarios_desde_archivo()
    while True:
        print("----- Aplicativo de Consola -----")
        print("1. Registro de nuevo usuario")
        print("2. Inicio de sesión")
        print("3. Listar usuarios")
        print("4. Listar roles")
        print("5. Ordenar usuarios")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        elif opcion == "3":
            listar_usuarios()
        elif opcion == "4":
            listar_roles()
        elif opcion == "5":
            ordenar_usuarios()
        elif opcion == "6":
            guardar_usuarios_en_archivo()
            respuesta = input("¿Desea continuar? (sí/si para volver al menú): ").lower()
            if respuesta in ["sí", "si"]:
                continue
            else:
                print("Gracias por usar el aplicativo. ¡Hasta luego!")
                break
        else:
            print("Opción no válida. Inténtalo nuevamente.\n")
        respuesta = input("¿Desea continuar? (sí/si para volver al menú): ").lower()
        if respuesta not in ["sí", "si"]:
            print("Gracias por usar el aplicativo. ¡Hasta luego!")
            break

