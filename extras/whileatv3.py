resultado = 0

while True:
    n1=float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite um segundo numero: "))

    while n2==0:
        print("0 é inválido!")
        n2=float(input())
    else:
        resultado=n1/n2
        print(resultado)
        break




