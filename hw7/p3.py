def findnumber(s):
	n = s.split()
	print(n)
	num = []
	for number in n:
		if number.isdigit():
			num.append(number)
	return num

sentence = "I am 18 years old and I have 3 cats and my brothers are 19 11 and 6"
num = findnumber(sentence)
print num

newsentence = findnumber(raw_input("type here: "))
print newsentence
