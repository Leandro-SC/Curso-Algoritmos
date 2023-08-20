from Class_Funciones import Funciones
from Class_Usuarios import Usuario
import re

def main():
    sistema = Funciones()

    #Ciclo repetitivo para mostrar las opciones del menu de consola
    while True:
        #Primero, comprueba el acceso del usuario
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        #Compara las opciones seleccionadas
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            correo = input("Ingrese el correo: ")
            #aplicamos una expresión regular para validar que tenga un formato valido de correo
            while not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
                print("Correo inválido. Intente nuevamente.")
                correo = input("Ingrese el correo: ")
            contraseña = input("Ingrese la contraseña: ")  # Obtener la contraseña del usuario
            roles = input("Ingrese los roles separados por comas: ").split(',')
            #instanciamos la clase usuario
            nuevo_usuario = Usuario(nombre, apellido, correo, contraseña, roles)
            #Almacenamos en json
            sistema.registrar_usuario(nuevo_usuario)
            print("Usuario registrado exitosamente.")
        elif opcion == "2":
            #comprueba las credeciales proporcionadas
            correo = input("Ingrese el correo: ")
            contraseña = input("Ingrese la contraseña: ")
            usuario_actual = sistema.login(correo, contraseña)
            if usuario_actual:
                print(f"Bienvenido, {usuario_actual.nombre}!")
                while True:
                    print("\nFunciones disponibles:")
                    print("1. Listar usuarios")
                    print("2. Listar roles")
                    print("3. Crear rol")
                    print("4. Ordenar usuarios")
                    print("5. Cerrar sesión")
                    opcion_usuario = input("Seleccione una opción: ")

                    if opcion_usuario == "1":
                        sistema.listar_usuarios(usuario_actual)

                    elif opcion_usuario == "2":
                        sistema.listar_roles(usuario_actual)

                    elif opcion_usuario == "3":
                        if 'admin' in usuario_actual.roles:
                            nuevo_rol = input("Ingrese el nuevo rol: ")
                            sistema.crear_rol(usuario_actual, nuevo_rol)
                        else:
                            print("Acceso denegado.")

                    elif opcion_usuario == "4":
                        descendente = input("Ordenar descendente (S/N)? ").upper() == "S"
                        sistema.ordenar_usuarios(usuario_actual, descendente)

                    elif opcion_usuario == "5":
                        print("Sesión cerrada.")
                        break
                    else:
                        print("Opción inválida.")

            else:
                print("Credenciales inválidas.")

        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()


