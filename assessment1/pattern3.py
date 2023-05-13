a,b=4,2
for i in range (1,4):
    if (i<=3):
        a = a - 1
        b = b + 1
    for j in range (1,6):
        if(j>=a and j<=b):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

