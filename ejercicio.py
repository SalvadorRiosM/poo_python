class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.name = nombre
        self.age = edad
        self.grade = grado
        
    def estudiar(self):
        print("Estudiando...")
    def aburrido(self):
        print("Estoy aburrido")
        
nombre = input("Nombre del estudiante: ")
edad = input("Cual es su edad? ")
grado = input("Cual es su grado? ")

estudiante1 = Estudiante(nombre, edad, grado)

print(f"""
      Datos del estudiante \n\n
      Nombre: {estudiante1.name}\n
      Edad: {estudiante1.age}\n
      Grado: {estudiante1.grade}\n
      """)

while True:
    estudiar = input("Escribe estudiar: ")
    if estudiar.lower() == "estudiar":
        estudiante1.aburrido()
        break
    else:
        print("Entrada no valida!")
        
        


