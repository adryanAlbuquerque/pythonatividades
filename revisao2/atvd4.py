n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
n3 = int(input("digite um numero: "))

if n1 > n2 and n1 > n3:
    print(n1,'é o maior numero!')
elif n2 > n1 and n2 > n3:
    print(n2,'é o maior numero!')
else:
    print(n3,'é o maior numero!')