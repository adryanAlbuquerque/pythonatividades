num_escolhido = 33
num = int(input("Adivinhe um numero de 1 á 100: "))

if num == num_escolhido:
    print("Parábens você acertou! o numero escolhido foi",num_escolhido)
elif num >= 101:
    print("Número inválido!")
else:
    print("Você errou!")