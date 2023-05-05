
while True:
    nota1 = int(input("Digite a primeira nota 0u digite (11) para sair "))
    if nota1 == 11:
        break
    nota2 = int(input("Digite a segunda nota: "))

    media = (nota1 + nota2) /2
    print("A media aritimerica de",nota1,"e",nota2,'é',media)
    resp = input("Deseja continuar? (sim/não): ")
    if resp == "não":
        break