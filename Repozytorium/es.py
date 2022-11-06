'''
================= zad 7 =============

for ciag in range (1,101):
    print(ciag, end=' ')

for ciag3 in range (7,78,7):
    print(ciag3, end=' ')

for ciag4 in range (20,-1,-2):
    print(ciag4, end=' ')

for ciag2 in range (100,-1,-1):
    print(ciag2, end=' ')

=================== zad 8 ===========
x=int(input("Podaj liczbe gwiazdek : "))
for g in range (x):
    print("*", end=' ')
'''

x=int(input("Podaj liczbe gwiazdek : "))
y=int(input("Podaj liczbe wierszy : "))
for z in range(y):
    for g in range(x):
        print("*", end=' ')
    print()