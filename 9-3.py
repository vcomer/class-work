fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened:', fname)
	exit()

counts = dict()
for line in fhand:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		if words[1] not in counts:
			counts[words[1]] = 1
		else:
			counts[words[1]] += 1

print(counts)
