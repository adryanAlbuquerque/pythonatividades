idade = int(input("Digite a sua idade: "))
estudante = input("Você é estudante? (S/N)".lower())

if idade >= 60 or estudante == "s":
    print("Você tem direito á meia entrada!")
else:
    print("Você não tem direito á meia entrada!")