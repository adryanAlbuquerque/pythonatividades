texto = ("o rato roeu a roupa do rei de roma")

vogais = 'aeiouAEIOU'

for x in texto:
    if x.lower() in vogais:
        print(x,end=" ")
