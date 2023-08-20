import bcrypt
import os
import json
from Class_Usuarios import Usuario


class Funciones:
    #Constructor
    def __init__(self):
        self._usuarios = []
        self.cargar_usuarios()

     #Metodo para registrar usuarios
    def registrar_usuario(self, usuario):
        self._usuarios.append(usuario)
        self._guardar_usuarios()

    #Metodo paraa guardar los usuarios en el archivo json
    def _guardar_usuarios(self):
        with open("usuarios.json", "w") as file:
            usuarios_data = []
            for usuario in self._usuarios:
                usuario_data = {
                    "nombre": usuario.nombre,
                    "apellido": usuario.apellido,
                    "roles": usuario.roles,
                    "correo": usuario.correo,
                    "password_hash": usuario.password,
                }
                usuarios_data.append(usuario_data)
            json.dump(usuarios_data, file)

    #Metodo para leer los usuarios almacenados en el archivo json
    def cargar_usuarios(self):
        try:
            with open("usuarios.json", "r") as file:
                usuarios_data = json.load(file)
                for usuario_data in usuarios_data:
                    usuario = Usuario(
                        usuario_data["nombre"],
                        usuario_data["apellido"],
                        usuario_data["correo"],
                        usuario_data["password_hash"],
                        usuario_data["roles"],
                    )
                    self._usuarios.append(usuario)
        except (FileNotFoundError, json.JSONDecodeError):
            pass 

    #Metodo para iniciar sesión        
    def login(self, correo, clave):
        for usuario in self._usuarios:
            if usuario.correo == correo and usuario.password == clave:
                return usuario
        return None

    #Metodo para listar usuarios
    def listar_usuarios(self, usuario_actual):
        if "admin" in usuario_actual.roles:
            for usuario in self._usuarios:
                print(
                    f"Nombre: {usuario.nombre} {usuario.apellido}, Roles: {', '.join(usuario.roles)}, Correo: {usuario.correo}"
                )
        else:
            for usuario in self._usuarios:
                print(
                    f"Nombre: {usuario.nombre} {usuario.apellido}, Correo: {usuario.correo}"
                )

    #Metodo para listar roles
    def listar_roles(self, usuario_actual):
        roles = set()
        for usuario in self._usuarios:
            roles.update(usuario.roles)
        print("Roles disponibles:")
        for rol in roles:
            print(rol)

    #Metodo para crear roles
    def crear_rol(self, usuario_actual, nuevo_rol):
        if "admin" in usuario_actual.roles:
            for usuario in self._usuarios:
                if nuevo_rol not in usuario.roles:
                    usuario.roles.append(nuevo_rol)
            print("Rol creado exitosamente.")
            self._guardar_usuarios()
        else:
            print("Acceso denegado.")

    #Metodo para ordenar en forma ascedente los usuarios si es administrador
    def ordenar_usuarios(self, usuario_actual, descendente=False):
        if "admin" in usuario_actual.roles:
            self._usuarios.sort(
                key=lambda usuario: (usuario.apellido, usuario.nombre),
                reverse=descendente,
            )
        else:
            print("Acceso denegado.")





