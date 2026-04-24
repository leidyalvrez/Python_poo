# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Departamento = ""
        self.__Asignaturas = ""

    def getDepartamento(self):
        return self.__Departamento
    
    def setDepartamentogt(self, Departamento):
        self.__Departamento = Departamento

    def getApellidos(self):
        return self.__Asignaturas
    
    def setApellidos(self, asignaturas):
        self.__Apellidos = asignaturas 

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)

class Profesor(Persona):
    pass

# metodo principal
def main():
    #Alumno 
    alumno = Alumno()
    alumno.setNombre("Leidy Yuliana")
    alumno.setApellidos("Alvarez Bravo")
    alumno.setEdad(17)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés"])
    alumno.mostrarAlumno()
    # Profesor
    profesor = profesor 
    profesor.setNombre("Nestor")
    profesor.setApellidos("Paez")
    profesor.setEdad(30)
    profesor.setDepartamento("Matematicas")
    profesor.setAsignatura(["Algebra", "Geometria"])
    profesor.mostrarProfesor()

if __name__ == "__main__":
    main()