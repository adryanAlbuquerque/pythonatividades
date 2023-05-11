


produto_list = []
preco_list = []


def inser(produto,preco):


    produto_list.append(produto)
    preco_list.append(preco)

while True:
    produto = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço: "))
    inser(produto,preco)

    decisao = input("Deseja inserir mais produtos? (sim ou nao): ")

    if decisao != "sim":
        print("Saiu")
        break

print(produto_list)
print(preco_list)


