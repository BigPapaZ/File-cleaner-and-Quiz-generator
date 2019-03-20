#######################
# cleanfooter.py
# Zaigham
# Deletes the last two lines of the input file
#######################

import sys

file_name = sys.argv[1]
output_file = sys.argv[2]

#reading the file
with open(file_name, "r") as f:
    plainText = f.readlines()
    f.close()

#Deleting the required lines
plainText.pop()
plainText.pop()


#writing the resulting file
with open(output_file, "w") as x:
    for i in plainText:
        x.write(i)
    x.close()