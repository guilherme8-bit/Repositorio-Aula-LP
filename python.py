import math
def Somar(x, y):
    return x + y

def Subtracao(x, y):
    return x - y

def Raiz_quadrada(x):
    return math.sqrt(x)

def main():
    x = int(input("Digite um número"))
    y = int(input("Digite um número"))
    print("Somar: ", Somar(x,y))
    print("Subtração: ", Subtracao(x,y))
    print("Raiz quadrada: ",Raiz_quadrada(x))