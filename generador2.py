import random
import string


class GeneradorContra:
    def __init__ (self):
        pass
    def contrasenia(self, num):
        caracter = []
        letra = []
        numero = []
        contraseña = []
        for x in range(1, int(num) + 1):
            i = random.choice(string.punctuation)
            caracter.append(i)
            i = random.choice(string.ascii_letters)
            letra.append(i)
            i = random.randint(0,9)
            numero.append(i)
#Suma las listaas
        contra = caracter + letra + numero
        print('\nEsta es tu contraseña\n')
    #Genera la contraseña aleatoriamente de las 3 listas
        for x in range(1, int(num) + 1):
            contraseña.append(random.choice(contra))
        print(*contraseña)
  
def run():
    GeneradorContra = GeneradorContra()
    num = input('Ingresa la cantida de digitos para tu contraseña: ')
    GeneradorContra.contrasenia(num)
 
if __name__ == '__main__':
    run()
    
    