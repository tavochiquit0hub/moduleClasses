class Alumno:
    def _init_(self):
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None
        self.__nombre_completo = None

    def set_nombre(self, nombre):
            self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
            self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
            self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
            self.__no_control = no_control

    def set_semestre(self, semestre):
            self.__semestre = semestre

    def set_nombre_completo(self, nombre_completo):
            self.__nombre_completo = nombre_completo

    # Métodos para obtener valores (getters)
    def get_nombre(self):
            return self.__nombre

    def get_apellido_paterno(self):
            return self.__apellido_paterno

    def get_apellido_materno(self):
            return self.__apellido_materno

    def get_no_control(self):
            return self.__no_control

    def get_semestre(self):
            return self.__semestre

    def get_nombre_completo(self):
            return self.__nombre_completo

    def get_nombre_completo_2(self):
            return self._nombre + " " + self.apellido_paterno + " " + self._apellido_materno