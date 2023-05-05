resp=5
while resp!=6:
    num=int(input("Digite o primeiro numero: "))
    num2=int(input("Digite um segundo numero: "))

    while True:
        resp= int(input("Escolha a operação: 1 - Soma// 2 - Subtrair // 3- Multiplicação // 4 - Dividir // 5 - Mudar numero // 6 - Sair "))

        match resp:
            case 1:
                print(num+num2)
            case 2:
                print(num-num2)
            case 3:
                print(num*num2)
            case 4:
                print(num/num2)
            case 5:
                break
            case 6:
                resp=6
                break
