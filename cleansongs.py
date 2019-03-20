#######################
# cleansongs.py
# Zaigham
# It cleans out some section of the data called songs.
#######################




import sys

file_name = sys.argv[1]
output_file = sys.argv[2]


#reads the file
with open(file_name, "r") as f:
    plainText = f.readlines()
    f.close()

#accumulator list
a=[]

#iteration thorugh the plain
for i in plainText:
    if i[0]==" " and i.upper()==i:    #checing to see if the line fills the required specifications
        continue                      #if the line does, then it is not appended to the output file
    else:
        a.append(i)                   #Appending the proper lines


#Writing the output
with open(output_file, "w") as x:
    for i in a:
        x.write(i)
    x.close()