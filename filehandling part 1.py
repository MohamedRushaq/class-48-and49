# write in file using with()function
with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am pengiun and I am 15 yr old. ")
file.close()

# splite file into words
with open('Codingal.txt', 'r') as file:
    data=file.readlines()
    print("Words in this file are...")
    for line in data:
     word = line.split()
    print (word)
file.close()  



