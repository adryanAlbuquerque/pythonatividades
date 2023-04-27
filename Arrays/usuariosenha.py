nomes = []
senha = []

for x in range(2):
    nomes.append(input("Digite o nome: "))
    senha.append(int(input("Digite a senha: ")))

for j in range(2):
    print("Usuário: ",nomes[j],"Senha:",senha[j],"-",j+1)