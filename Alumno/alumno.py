
#Agregar test para clase Materia y Profesor incluyendo test de constructor y demás metodos
#La clase materia deberia tener un atributo __ alumnos __ equivalente a una lista de Alumnos. Empezando por los tests:
#Implementar la clase Alumno>>>>
#Agregar atributo __ alumno __ a clase Materia>>>>
#Agregar metodo obtener_alumnos(self) que devuelva __ alumnos __>>>>
    
class Alumno:
    def __init__(self, nombre, edad, legajo):
        self.__nombre__ = nombre
        self.__edad__ = edad
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_edad(self):
        return self.__edad__

    def obtener_legajo(self):
        return self.__legajo__

    def falta(self):
        self.__inasistencias__ +=1    

    def esta_libre(self):
        if self.__inasistencias__ >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"