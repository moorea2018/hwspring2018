temp = float(raw_input("please enter your body tempreture: "))
normal = 98.6
hot = 99
cold = 96

if (temp == normal):
	print("Congratulations, you are normal and healthy!")
elif(temp > cold and temp < hot):
	print("close to normal, you may want to try again later")
elif (temp > hot or temp == hot):
        print ("Do you feel warm?")
	yousure = raw_input("please enter yes or no: ")
	if(yousure.lower() == "no"):
		print ("you must be warm blooded")
	elif(yousure.lower() == "yes"):
		print ("you may be running a fever...")
elif(temp < cold or temp == cold):
        print ("Do you feel cold?")
	yousure = raw_input("please enter yes or no: ")
	if(yousure.lower() == "no"):
		print ("hmph, you must be cold blooded")
	elif(yousure.lower() == "yes"):
		print ("try dressing up for the winter to keep your temperature up")
