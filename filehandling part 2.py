#creat a new file 
new_file=open('New_File1.txt', 'x')
new_file.close()

#check if a file exists
import os
print("Checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exist")

#creat a new if it doesn't
my_file=open("my_file.txt", "w")
my_file.write("Hi! I am pengiun and I am 15 yr old.")
my_file.close()        