num = int(input("Digite um numero: "))


if num == 0:
    print("O numero é 0!")

elif num % 2 == 0 and num > 0:
    print(num,"é um numero par positivo!")
elif num % 2 != 0 and num > 0:
    print(num,"é um numero ímpar positivo!")

elif num % 2 == 0 and num < 0:
    print(num,"é um numero par negativo!")
else:
    print(num,"é um numero ímpar negativo!")