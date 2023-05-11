texto = ("o rato roeu a roupa do rei de roma")

def quant_vogais(texto2):

    vogais = 'aeiouAEIOU'
    cont = 0

    for x in texto:
        if x in vogais:
            cont+=1
    print(f"a quantidade de vogais é {cont}")

quant_vogais(texto)