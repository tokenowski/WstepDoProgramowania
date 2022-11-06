l1 = int(input("Liczba 1 = "))
l2 = int(input("Liczba 2 = "))

if(l1>l2):
    w=l1
    m=l2
else:
    w=l2
    m=l1

while(m<=w):
    print(m, end=' ')
    m=m+1