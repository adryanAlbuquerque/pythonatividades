inicio = int(input("Qual hora começa o jogo?: "))
fim = int(input("Qual hora termina o jogo?:"))

duracao = fim + 24 - inicio

if duracao < 24:
    print(duracao,"horas de jogo!")

else:
    print(fim - inicio, "horas de jogo")
