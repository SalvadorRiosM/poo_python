# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# Múltiplos de multiplo3 por la palabra "fizz".
# Múltiplos de mul por la palabra "buztimultiplo5z".
# Múltiplos de multiplo3 y de mul a la vez por la paltimultiplo5abra "fizzbuzz".

multiplo3 = 3
multiplo5 = 5

def fizzbuzz():
  for numero in range(1, 101):
        if numero % multiplo3 == 0 and numero % multiplo5 == 0:
            print("fizzbuzz")
        elif numero % multiplo3 == 0:
            print("fizz")
        elif numero % multiplo5 == 0:
            print("buzz")
        else:
            print(numero)
            
fizzbuzz()