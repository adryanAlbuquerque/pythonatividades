
a = []
i = 0

impar = 0

while True:
    if i % 2 != 0:
        a.append(i)
        impar += 1

    if impar == 10:
     break
    i +=1

print(a)