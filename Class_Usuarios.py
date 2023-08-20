class Usuario:
    #Constructor de la clase y sus atributos
    def __init__(self, nombre, apellido, correo, password, roles):
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._password = password 
        self._roles = roles

    #Metodos Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @property
    def password(self):
        return self._password 

    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, nuevos_roles):
        self._roles = nuevos_roles
