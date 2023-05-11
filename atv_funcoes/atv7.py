def estoq(produto,quantidade,valor):
    return  produto,quantidade*valor

total = estoq("Cuscuz", 2, 3.5)

print(f"O valor do {total[0]} é {total[1]} reais")