def escada(n):
    for x in range(1,n+1):
        for i in range(1,x+1):
            print(i,end=" ")
        print()
escada(10)
