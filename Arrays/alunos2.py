quantidade = int(input("digite numero de alunos: "))
alunos=[]
for x in range(quantidade):
    alunos.append(input("Digite o nome do aluno: "))


for y in range(quantidade):
    print(alunos[y],y)

