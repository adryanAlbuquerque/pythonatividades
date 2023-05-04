i = 0

while i < 1:

    num1 = int(input("Digite seu primeiro numero: "));
    num2 = int(input("Digite o segundo numero: "));
    if  num1 != num2:

        if num1 > num2:
            print(num2,num1);
        else:
            print(num1,num2)

    else:
        print("Numeros iguais");

    resp = input("Deseja fazer denovo (sim/não): ")
    if resp=="não":
        break

