#Grade Exercise
x = float(raw_input ('Please enter the grade '))
if x > 1.0:
	print ('Grade too high')
elif x >= .90:
	print ('A')
elif x >= .80:
	print ('B')
elif x >= .70:
	print ('C')
elif x >= .60:
	print ('D')
elif x < .60 and x > 0.0:
	print ('F')
elif x <= 0.0:
	print ('Grade too low')
	