file=open('abc.txt','r')
print(file.read())
file.close()


file=open('abc.txt', 'w')
file.write("Hi today is great ")
file.close()


file=open('abc.txt', 'a')
file.write("Education is good")
file.close()

file=open('abc.txt', 'r')
print("Looping through the lines...")
for line in file:
    print(line)
file.close()    