fname = input("Enter file name: ")
fhand = open(fname)
words = []
for line in fhand:
	list = line.split()
	for word in list:
		if word in words: continue
		words.append(word)
words.sort()
print(words)