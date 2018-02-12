fname = ('mbox-short.txt')
try:
	fhand = open(fname)
except:
	print("File not found: ", fname)
	quit()
try:
	for line in fhand:
		words = line.split()
		if len(words) == 0 : continue
		if words[0] != 'From' : continue
		print(words[2])
except:
	print("File: ", fname, "not properly guarded.")
	quit()
	

