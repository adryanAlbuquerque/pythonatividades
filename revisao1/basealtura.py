while True:
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))

    A = base * altura / 2
    print("O resultado é:", A)
    resp =input("Deseja continuar?")
    if resp =="não":
        break