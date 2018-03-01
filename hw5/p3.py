string = raw_input("please type a sentence seperating each word with a comma :")
lower = string.lower()
split = string.split(",")
characters = len(string)
words = string.split(",")
number = len(words)

if((number % 2) != 0 and string.find("llama") != -1):
	print split
elif((len(string)%2) == 0 or (number % 2) != 0):
	print ("That is odd")
