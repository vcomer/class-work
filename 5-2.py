largest = None
smallest = None
while True :
	sval = input('Enter a number: ')
	if sval == 'done' : break
	try:
		fval = float(sval)
	except:
		print('Invalid input')
		continue
	if smallest is None or fval < smallest:
		smallest = fval
	if largest is None or fval > largest:
		largest = fval
			
print ("Maximum is", largest)
print ("Minimum is", smallest)
