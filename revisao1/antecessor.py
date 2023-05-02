num = int(input("Digite um numero: "))
antposi = num - 1

antneg = num + 1


if num >= 0:
    print("O numero",num,"tem como antecessor",antposi)
else:
    print("O numero",num,"tem como antecessor",antneg)