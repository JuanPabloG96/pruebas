class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def __info__(self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)