class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.name = nombre
        self.age = edad
        self.nationality = nacionalidad
    
    def hablar(self):
        print("estoy hablando un poco")
        
        
class Empleado(Persona):        # La clase empleado hereda todas las propiedades de la clase Persona
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.work = trabajo
        self.salary = salario
        
#    def hablar(self):                   # Reescribio el metodo de hablar!!
#       print("No quiero hablar")

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.grades = notas
        self.univercity = universidad
       
roberto = Empleado("Roberto", 35, "Argentino", "Programador", "50,000")

roberto.hablar()


