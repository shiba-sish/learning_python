# creating a text file and writing inside it
f= open("C:/Users/Shibasish China/Desktop/python.programming.txt","r") #w(write) is the mode of the file and a(append) add line after line
# mynotes= f.read()
# mynotes= f.read(10)
# mynotes= f.readline()
mynotes= f.readlines()
print(mynotes)
print(len(mynotes))
f.close()

