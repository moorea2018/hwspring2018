currentNumber = int(raw_input("Please enter an integer value: "))

if(currentNumber % 2 == 0):
	evennumber = (currentNumber/2)
	print "new number is..."
	print evennumber
elif(currentNumber % 2 != 0):
	oddnumber = ((currentNumber*3)+1)
	print "new number is..."
	print oddnumber

