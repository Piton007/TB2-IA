import sys
sys.path.append("D:\\Enciclopedia\\Universidad\Inteligencia Artificial\\TB2\\TB2-IA\\Src")
from PerceptronMultiCapa import PerceptronMulticapa

def calcular_salida(a,b,c,d):
    entradas=[a,b,c,d]
    salidas = []
    if a and b and c :
        salida = 1
    elif a and ((b or c) and d):
        salida = 1
    else:
        salida = 0
    salidas.append(salida)
    return [entradas,salidas]

def generar_posibilidades(numero_atributos):
    filas=numero_atributos**2
    limite_binario=len(str(bin(filas-1)[2:]))
    combinaciones=[ map(lambda i: int(i),list(bin(x)[2:].zfill(limite_binario)))  for x in range(filas) ]
    return combinaciones

atributos=input("Inserte numero de atributos: ")

patrones=[]
entradas=[]
resultados=[]
for posibilidad in generar_posibilidades(int(atributos)):
    a,b,c,d=[_ for _ in posibilidad]
    patrones.append(calcular_salida(a,b,c,d))
for  entrada,resultado in patrones:
    entradas.append(entrada)
    resultados.append(resultado)
neurona=PerceptronMulticapa(entradas,resultados,100,0.25,0.6)
neurona.test(int(atributos),2,1)

    
