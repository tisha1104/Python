lines=5
for i in range(1,lines+1):
    for j in range(1,lines+1):
        if i%2==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()