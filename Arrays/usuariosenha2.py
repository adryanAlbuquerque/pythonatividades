usuario = []
senha = []

for x in range(1):
    usuario.append(input("Digite o usuario: "))
    senha.append(input("Digite a senha: "))

loginusuario = (input("Digite seu usuário para login: "))
loginsenha = (input("Digite sua senha para login: "))

for y in range(1):
    if usuario[y]==loginusuario and senha[y] == loginsenha:
        print("Login feito")

    else:
        print("Login Inválido!")
