def computepay(hours, rate):
	print("In computepay", hours, rate)
	if fh > 40:
		print("Overtime")
		reg = hours * rate
		otp = (hours - 40.0) * (rate * 1.5)
		pay = reg + otp
	else:
		pay = hours * rate
	print("Returning", pay)
	return pay
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
xp = computepay(fh, fr)
print("Pay:", xp)
