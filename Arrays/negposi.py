

while True:
    num = int(input("Digite um numero diferente de zero: "))

    if num == 0:
        print("Numero inválido!")

    elif num > 0:
        print(num, "é positivo!")

    else:
        print(num,"é negativo!")
    resp =input("Deseja continuar?")
    if resp =="não":
        break