#######################
# cleandorections.py
# Zaigham
# Cleans out the directions in the play
#######################


import sys

file_name = sys.argv[1]
output_file = sys.argv[2]

#reading the file
with open(file_name, "r") as f:
    plainText = f.readlines()
    f.close()


#An accumulator list
newlist=[]
#An accumulator
acc=0



#Directions being cut out from the data
for x in range(len(plainText)):
    newlist.append(plainText[x])

    if plainText[x][0] == "[": acc=1  #Start cutting from here

    if acc==1: newlist.remove(plainText[x])   #Here the actual cutting occurs

    if plainText[x][-2] == "]": acc=0     #Stop cutting here


#Output being written
with open(output_file, "w") as x:
    for i in newlist:
        x.write(i)
    x.close()