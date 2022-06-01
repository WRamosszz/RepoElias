#_______SORTEAR VALORES ALEATORIOS________
import random

a = int(input("Valor 1:"))
b = int(input("Valor 2:"))

if(a > b):
    c = a
    a = b
    b = c

x1 = random.randint(a, b)
x2 = random.randint(a, b)

if(x1 > x2):
    print("maior valor é:", x1)
elif(x1 < x2):
    print("menor valor é", x2)
 

 
"""#_____________mostrar o tempo de espera____1
import time
print("Gerando números")
time.sleep(1)"""


"""#_______________calcular raizes__________10
import math
num = int(input("Valor: "))

r = math.sqrt(num) # raiz quadrada
p = math.pow(num, 2) # potencia
f = math.floor(8.42) # arredondar o valor para baixo
c = math. ceil(8.102) #arredondar o valora para cima
j = round(8.42, 1)

print("Raiz de", num, "é", r)
print(num, "elevado a 3 é", p)
print("Piso de 8,96 é", f)
print("Teto de 8,102 é", C)""'"""