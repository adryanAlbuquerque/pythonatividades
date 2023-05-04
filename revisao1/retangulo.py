resp = int(input("Digite: 1 p/ Calcular o Triangulo || 2 p/ Retangulo: "))

while resp == 1:
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))

    A = base * altura / 2
    print("O triangulo é:", A)
    resp1 =input("Deseja sair (sim/não): ")
    if resp1 =="sim":
        break

while resp == 2:
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))

    B = base * altura
    print("O retangulo é:", B)
    resp1 =input("Deseja sair (sim/não): ")
    if resp1 =="sim":
        break

while resp <= 0 and resp >= 3:
    print("Inválido!")