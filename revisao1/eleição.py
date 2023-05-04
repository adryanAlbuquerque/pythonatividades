eleitores = int(input("Digite o numero de eleitores: "))
brancos = int(input("Digite o numero de votos brancos: "))
nulos = int(input("Digite o numero de votos nulos: "))
validos = int(input("Digite o numero de votos válidos: "))


calc1 = (brancos / eleitores) * 100
calc2 = (nulos / eleitores) * 100
calc3 = (validos / eleitores) * 100


if calc1 + calc2 + calc3 > 100:
    print("Inválido! houve fraude")

elif calc1 + calc2 + calc3 < 100:
    print("Inválido! houve fraude")


else:
    print(calc1, "Porcento dos votos branco")
    print(calc2, "Porcento dos votos nulo")
    print(calc3, "Porcento dos votos validos")
    print("Total de eleitores:", eleitores)



