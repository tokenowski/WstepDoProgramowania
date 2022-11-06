'''
x=-4
while x<= 4:
    print(f"f({x}) = {2*x**2-5*x-8}")
    x=x+0.5
'''

'''
while True:
    x=int(input("Podaj liczbe: "))
    if (x<0): break

'''

liczba1 = int(input("Liczba 1: "))
liczba2 = int(input("Liczba 2: "))
if(liczba1 > liczba2):
    wieksza = liczba1
    mniejsza = liczba2
else:
    wieksza = liczba2
    mniejsza = liczba1
while(mniejsza <= wieksza):
    if mniejsza%2==1:
        mniejsza+=1
        continue
    print(mniejsza, end=' ')
    mniejsza = mniejsza + 1