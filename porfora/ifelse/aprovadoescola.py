nota = float(input("Qual fou sua nota?: "))

if nota > 10 :
    print("Nota inválida!")

elif nota >= 6:
    print("Aluno aprovado com a nota :", nota)
else:
    print("Aluno reprovado com a nota :", nota)