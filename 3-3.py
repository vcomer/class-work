try:
	score = float(input('Enter 0.0 to 1.0: '))
	if score >= 0.0 and score <= 1.0:
		pass
	else:
		print("Score out of range. Retry.")
		quit()
except:
	print("Bad Score")
	quit()
if score >= 0.9:
	print("A")
elif score >= 0.8:
	print("B")
elif score >= 0.7:
	print("C")
elif score >= 0.6:
	print("D")
else:
	print("F")
quit()


