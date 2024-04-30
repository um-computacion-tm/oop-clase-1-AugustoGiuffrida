class Materia:
    def __init__(self, nombre, profesores, alumnos):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__
    
    def obtener_alumnos(self):
        return self.__alumnos__
        
    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre