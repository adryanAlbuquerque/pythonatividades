lista = []

confirm = 's'
while confirm =='s':
    num1 = int(input("Digite um numero: "))
    num2= int(input("Digite um outro numero: "))

    media = num1 + num2 / 2

    if media >= 7:
        print("Aprovado com a nota ",media)
    elif media >=4:
        print("Em recuperação com a nota", media)
    else:
        print("Reprovado com a nota: ",media )
    confirm = input('quer continuar? S/N').lower()[0]