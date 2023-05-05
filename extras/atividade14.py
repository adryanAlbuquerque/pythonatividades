num1 = int(input("Digite um numero maior que zero: "))
if num1>0:
    for x in range(1, num1 + 1, 1):
        print(x)
else:
    print("Numero inválido!")