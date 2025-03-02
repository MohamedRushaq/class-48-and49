# creating the output file
outputfile=open('Updatedfile.txt', 'w')

# reading the input file
inputfile=open('Repeated.txt' "r")

# holds lines already seen
lines_seen_so_far=set()
print("eliminating duplicate lines....")
# iterating each line in the file
for line in inputfile:

    # checking if line is unique
    if line not in lines_seen_so_far:
        # write unique lines in outpput file
        outputfile.write(line)

        # adds unique lines to lines_seen_so_far
        lines_seen_so_far.add(line)


# cloasing the file 
inputfile.close()
outputfile.close()        