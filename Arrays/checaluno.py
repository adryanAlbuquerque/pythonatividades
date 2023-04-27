quantidade = int(input("digite numero de alunos: "))
alunos = []
for x in range(quantidade):
    alunos.append(input("Digite o nome do aluno: "))

checagem=input("Pesquise um nome: ")
for y in range(quantidade):
    if checagem==alunos[y]:
        print(y, alunos[y])
    else:print("Não está na lista!")