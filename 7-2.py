fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened: ', fname)
	exit()
count = 0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):
		count = count + 1
print("Average spam confidence: ", count, fname)

