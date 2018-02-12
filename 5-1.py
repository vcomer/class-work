total = 0
count = 0.0
while True :
	sval = input('Enter a number: ')
	if sval == 'done' :
		break
	try:
		fval = float(sval)
	except:
		print('Invalid input')
		continue
	total = total + 1
	count = count + fval
	
print (count, total, count/total)