#temperature converter
x = raw_input ("C or F? ")
y = int(raw_input ("What Degree to Convert? "))

if x == 'F':
	TempC = (y - 32) * .5556
	print 'Temperature=', TempC, 'Celsius'

if x == 'C':
	TempF = (y * 1.8) + 32
	print 'Temperature=', TempF, 'Fahrenheit'