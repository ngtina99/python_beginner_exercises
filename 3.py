sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
fh = float(sh)
fr = float(sr)

if fh > 40:
	reg = fh * fr
	otp = (fh - 40.0) * (fr *0.5)
	print(reg, otp)
	xp = reg + otp
else:
	xp = fh *fr
print('Pay: ', xp)