#######################
# cleanblanks.py
# Zaigham
# Rewrites a file without any blank lines
#######################


import sys

file_name = sys.argv[1]
output_file = sys.argv[2]

#reading the file
with open(file_name, "r") as f:
    plainText = f.readlines()
    f.close()

#filtering out the empty lines
for aline in plainText:
    if aline=="\n":
        plainText.remove("\n")
        try:
            plainText.pop(plainText.index("\n"))
        except: pass

#writing to the output file
with open(output_file, "w") as x:
    for aline in plainText:
        x.write(aline)
    x.close()