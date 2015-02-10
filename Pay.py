#Pay Calculator
Rate = raw_input ('How much do you make per hour? ')
Hours = raw_input ('How many hours did you work? ')
if float(Hours) <= 40.0:
	x = float(Rate) * float(Hours)
	print ('Your pay is'), x
elif float(Hours) > 40:
	x = (float(Rate) * 40) + ((float(Hours) - 40) * 1.5)
	print ('Your pay is'), x