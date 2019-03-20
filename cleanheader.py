#######################
# cleanheader.py
# Zaigham
# Cleans out the a specific section of the input text file upto a certain point.
#######################




import sys

file_name = sys.argv[1]
output_file = sys.argv[2]


#Reading the file
with open(file_name, "r") as f:
    plainText = f.readlines()
    f.close()

#accumulator which will help determine when 'ACT I' pops up being setup
acc1=0
acc2=0

#Those previously mentioned accumulators in action
for i in range(len(plainText)):
    acc1+=1
    if "ACT I." in plainText[i]:
        acc2=acc1
        break


#the whole text without the header part
newTEXT=plainText[acc2:]



with open(output_file, "w") as x:
    #the title of the play being written
    x.write( plainText[0][27:plainText[0].index("by")]+"\n" )
    #the rest of the file being written
    for i in newTEXT:
        x.write(i)
    x.close()