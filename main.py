class persona:    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def __info__(self):
        print("\nInformación almacenada del usuario: ")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellido}")
        print(f"Edad: {self.edad} años")

nombre = input("\nEscribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
edad = input("Escribe tu edad: ")

p1 = persona(nombre, apellido, edad)

p1.__info__()