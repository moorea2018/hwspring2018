def findupper(s):
        words = s.split()
        upperwords = []
        for letter in words:
                if letter.istitle():
                        upperwords.append(letter)
        return upperwords

sentence = "My name is Alex moore"
upperwords = findupper(sentence)
print upperwords


userUpperWords = findupper(raw_input("enter a sentence"))
print userUpperWords
def findupper(s):
	words = s.split()
	upperwords = []
	for letter in words:
		if letter.istitle():
			upperwords.append(letter)
	return upperwords

sentence = "My name is Alex moore"
upperwords = findupper(sentence)
print upperwords


userUpperWords = findupper(raw_input("enter a sentence"))
print userUpperWords
