s_hour = input('Enter Hours: ')
s_rate = input('Enter Rate: ')
f_hour = float(s_hour)
f_rate = float(s_rate)

if f_hour > 40:
	reg = f_hour * f_rate #regular pay
	otp = (f_hour - 40.0) * (f_rate *0.5) #overtime pay
	print(reg, otp)
	xp = reg + otp #expended, total pay
else:
	xp = f_hour *f_rate
print('Pay: ', xp)