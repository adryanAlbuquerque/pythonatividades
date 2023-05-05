alunos = 0
soma = 0

NAlunos = int(input("Digite a quantidade de alunos: "))
while alunos < NAlunos:
    notaAlunos = float(input("Digite a nota: "))
    soma = soma + NAlunos
    alunos +=1

print("A media da classe é", soma / NAlunos)