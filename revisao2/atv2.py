
while True:
    n1 = int(input("Digite um numero: "))
    if n1 != 0:
        if n1 > 0:
            print("Numero",n1,"é positivo!")
        else:
            print("Numero",n1,"é negativo!")
    else:
        print("0 é invalido!")
    resp = input("Deseja sair? (sim/não) ")
    if resp == "sim":
        break