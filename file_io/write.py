import re

f = open('data.txt','r+')
line = "A new line"

# Overwrite first line
f.write(line)

# Overwrite 3rd line
f.seek(34)
f.write(line)

# Append a 5th line
f.seek(0,2)
f.write('\n' + line)

f.close()