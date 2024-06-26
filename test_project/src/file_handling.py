# Open a file in write mode\
file = open('newFile.txt', 'w')
file.write("This is a new file\nHello\n")
file.close()

# Open a file in read mode
file = open('newFile.txt', 'r')
content = file.read()
print(content)
file.close()

# Open a file in append mode
file = open('newFile.txt', 'a')
file.write("This is the 3rd line!\n")
file.close()

file = open('newFile.txt', 'r')
content = file.read()
print(content)
file.close()

# With statement

with open('newFile.txt','a') as file:
    file.write("4th line now!")

with open('newFile.txt','r') as file:
    content = file.read()
    print(content)

