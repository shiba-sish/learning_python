# creating a text file and writing inside it
f= open("C:/Users/Shibasish China/Desktop/python.programming.txt","a") #w(write) is the mode of the file and a(append) add line after line
notes='''for i in range(1,6):
    for i in range(1,6):
        print("*", end=" ")
    print() \n
    for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
'''
f.write(notes)
f.close()

