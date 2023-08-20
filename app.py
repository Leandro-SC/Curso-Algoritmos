from Class_Funciones import Funciones
from Class_Usuarios import Usuario
import re
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    sistema = Funciones()

    while True:
        clear_console()

        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Código para registrar usuario
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            correo = input("Ingrese el correo: ")
            while not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
                print("Correo inválido. Intente nuevamente.")
                correo = input("Ingrese el correo: ")
            contraseña = input("Ingrese la contraseña: ")
            roles = input("Ingrese los roles separados por comas: ").split(',')
            nuevo_usuario = Usuario(nombre, apellido, correo, contraseña, roles)
            sistema.registrar_usuario(nuevo_usuario)
            print("Usuario registrado exitosamente.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            # Código para iniciar sesión
            correo = input("Ingrese el correo: ")
            contraseña = input("Ingrese la contraseña: ")
            usuario_actual = sistema.login(correo, contraseña)
            if usuario_actual:
                print(f"Bienvenido, {usuario_actual.nombre}!")

                while True:
                    clear_console()
                    print("Funciones disponibles:\n")
                    print("1. Listar roles")
                    print("2. Listar usuarios")
                    if "admin" in usuario_actual.roles:  
                        print("3. Crear rol")
                        print("4. Ordenar usuarios")
                        print("5. Cerrar sesión")
                    else:
                        print("3. Cerrar sesión")

                    opcion_usuario = input("Seleccione una opción: \n")

                    if "admin" in usuario_actual.roles:
                        if opcion_usuario == "1":
                            sistema.listar_roles(usuario_actual)
                        elif opcion_usuario == "2":
                            sistema.listar_usuarios(usuario_actual)
                        elif opcion_usuario == "3":
                            nuevo_rol = input("Ingrese el nuevo rol: ")
                            sistema.crear_rol(usuario_actual, nuevo_rol)
                        elif opcion_usuario == "4":
                            descendente = input("Ordenar descendente (S/N)? \n").upper() == "S"
                            sistema.ordenar_usuarios(usuario_actual, descendente)
                        elif opcion_usuario == "5":
                            print("Sesión cerrada.")
                            break
                        else:
                            print("Opción inválida.")
                    else:
                        if opcion_usuario == "1":
                            sistema.listar_roles(usuario_actual)
                        elif opcion_usuario == "2":   
                            sistema.listar_usuarios(usuario_actual)
                        elif opcion_usuario == "3":
                            print("Sesión cerrada.")
                            break
                        else:
                            print("Opción inválida.\n")
                    input("Presione Enter para continuar...")

            else:
                print("Credenciales inválidas.\n")
                input("Presione Enter para continuar...")

        elif opcion == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
