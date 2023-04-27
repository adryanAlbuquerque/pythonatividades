A = []
B = []
C = []

n = int(input("Digite um numero: "))
for x in range(n):
    A.append(int(input("Informe o numero para A")))
    B.append(int(input("Informe o numero para B")))


for y in range(n):
    C.append(A[y]+B[y])
print(A)
print(B)
print(C)