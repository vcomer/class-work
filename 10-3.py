
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
letters = dict()
for line in fhand:
    line = line.lower()
    for x in line: 
        if x not in 'abcdefghijklmnopqrstuvwxyz': continue
        if x not in letters:
            letters[x] = 1
        else:
            letters[x] += 1

# Sort the dictionary by value
lst = list()
for key, val in letters.items():
    lst.append( (val, key) )
lst.sort(reverse = True)

for key, val in lst :
    print(key, val)