nota = int(input("Digite sua nota de 1 á 10: "))
nota2 = int(input("Digite sua segunda nota de 1 á 10: "))

media = nota + nota2 / 2

if media >= 6:
    print("Aprovado! com media",media)
else:
    print("Reprovado com media",media)
