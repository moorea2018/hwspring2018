import random

player1 = raw_input ("Please enter player1 name")
player2 = raw_input ("Please enter player2 name")
player3 = raw_input ("Please enter player3 name")
beginning = 1
end = 9
score1 = 0
score2 = 0
score3 = 0
roll1 = (beginning,end)
roll2 = (beginning,end)
roll3 = (beginning,end)
roll4 = (beginning,end)
roll5 = (beginning,end)
roll6 = (beginning,end)
roll7 = (beginning,end)
roll8 = (beginning,end)
roll9 = (beginning,end)
rollresult1 = (roll1 + roll2 + roll3)
rollresult2 = (roll4 + roll5 + roll6)
rollresult3 = (roll7 + roll8 + roll9)

def roll(beginning,end):
	return random.randint(beginning,end)
#3 rolls that will add up.
def roundWinner(rollresult1,rollresult2,rollresult3):
	if(rollresult1 == 21):
		return "Player1 wins the round"
	elif(rollresult2 == 21):
		return "Player2 wins the round"
	elif(rollresult3 == 21):
		return "Player3 wins the round"

def gameWinner(score1,score2):
	if(score1 > score2):
		return "Player 1 Wins the Game"
	elif(score2 > score1):
		return "Player 2 Wins the Game"
	elif(score3 > 2):
		return "Tie Breaker"

while score1 < 3 and score2 < 3 and score3 < 3:
	roll1 = roll(beginning,end)
	roll2 = roll(beginning,end)
	roll3 = roll(beginning,end)
	roll4 = roll(beginning,end)
	roll5 = roll(beginning,end)
	roll6 = roll(beginning,end)
	roll7 = roll(beginning,end)
	roll8 = roll(beginning,end)
	roll9 = roll(beginning,end)
	rollresult1 = (roll1 + roll2 + roll3)
	rollresult2 = (roll4 + roll5 + roll6)
	rollresult3 = (roll7 + roll8 + roll9)
	print (rollresult1,rollresult2,rollresult3)
	if rollresult1 == 21:
		score1 += 1
		print player1
		print "Wins The Game"
	elif rollresult2 == 21:
		score2 += 1
		print player2
		print "Wins The Game"
	elif rollresult3 == 21:
		score2 += 1
		print player3
		print "Wins The Game"
if score1 > 2 or score2 > 2 or score3 > 2:
	print ("Final Results")
	print (score1,score2,score3)
	if score1 == 3:
		print player1
		print "Wins The Match"
	elif score2 == 3:
		print player2
		print "Wins The Match"
	elif score3 == 3:
		print player3
		print "Wins The Match"
