class Celular:
    def __init__(self, marca, modelo, camara):  # Parametros
        self.marca = marca                      # Propiedad marca = al parametro
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estas haciendo una llamada de un: {self.modelo}")
        
    def colgar(self):
        print(f"Estas colgando tu llamada desde un: {self.modelo}")

celular1 = Celular("Samsun", "S23", "48Mp")     # 3 Argumentos al objeto celular1
celular2 = Celular("Apple", "Iphone", "96Mp") 

celular1.llamar()



        