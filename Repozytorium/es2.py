'''
====================== zad 1 =============
L=['bulka','chleb','mleko','woda','jablko']
print(L[0]+ ", "+L[1])
L[1]="maslo"
print(L[0]+ ", "+L[1])
print(L[-1]+", "+L[-2])
====================== zad 2 ==============

import random
x=int(input("Podaj ilosc liczb : "))
zestaw1=[]
for i in range(x):
    n = random.randint(1,10)
    zestaw1.append(n)
print(zestaw1)

x2=int(input("Podaj ilosc liczb : "))
zestaw2=[]
for i in range(x2):
    n2 = random.randint(1,10)
    zestaw2.append(n2)
print(zestaw2)

x3 = int(input("Podaj liczbe ktorej szukasz : "))
if x3 in zestaw1:
    print("Wystepuje w liscie 1")
elif x3 in zestaw2:
    print("Wystepuje w liscie 2")
else:
    print("Nie ma takiej liczby")

zestaw1_2 = zestaw1 + zestaw2

zestaw1_2.sort()
print (zestaw1_2)

========================== zad 3 ========



'''

zwierzeta = []
for x in range (7):
   n = input("Podaj nazwe : ")
   zwierzeta.append(n)

zwierzeta.sort()
print (zwierzeta)

print(zwierzeta[-0]+zwierzeta[-1]+zwierzeta[-2]+zwierzeta[-3])