class persona:

    # Metodo constructor de la clase 
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre 
        self.apellido = apellidos
        self.edad = edad 

# Metodo para mostrar la informacion de la persona: 
    def mostrarPersona(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellidos)
        print("Edad: ", self.edad)

def main():
    print("vamos a aprender POO...")

if __name__ == main():
    main()