def somar (n1,n2):
    return (n1+n2)

def sub (n1,n2):
    return (n1-n2)

def multi (n1,n2):
    return (n1*n2)

def dividir (n1,n2):
    return (n1/n2)


while True:

    decisao = int(input(" 1 - Somar \n 2 - Subtrair \n 3 - Multiplicar \n 4 - Dividir \n 5 - Sair \n Responda: "))
    while decisao > 5:
        decisao = int(input(" 1 - Somar \n 2 - Subtrair \n 3 - Multiplicar \n 4 - Dividir \n 5 - Sair \n Responda: "))

    if decisao == 5:
        print("Saiu")
        break
    n1 = int(input("Digite um numero:"))
    n2 = int(input("Digite um outro numero:"))




    if decisao == 1:
        print(somar(n1,n2))

    elif decisao == 2:
        print(sub(n1,n2))

    elif decisao == 3:
        print(multi(n1,n2))

    elif decisao == 4:
        print(dividir(n1,n2))

