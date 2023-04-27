dentro = 0
fora = 0

for x in range(10):
   num1 = int(input("Digite um numero: "))
   if num1 >= 10 and num1<=20:
      dentro+=1
   else:
      fora=fora+1

print("Foram",dentro,"numeros dentro e",fora, "numeros fora")
