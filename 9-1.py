fname = 'words.txt'
fhand = open(fname)
d = dict()
for line in fhand:
    words = line.split()
    
print(d)
print ("would" in d)
print ("fast" in d)
print ("python" in d)