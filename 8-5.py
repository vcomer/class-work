fname = 'mbox-short.txt'
try:
	fhand = open(fname)
	count = 0
except:
	print("File not found: ", fname)
	exit()
try:
	count = 0
	for line in fhand:
		words = line.split()
		if not len(words) == 0 and words[0] == 'From' : print(words[1])
		count = count + 1
except:
	print("File: ", fname, "not properly guarded.")
	exit()
print("There were", count, "lines in the file with From as the first word.")