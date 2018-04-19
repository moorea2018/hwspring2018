import random

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

while score1 < 2 and score2 < 2 and score3 < 2:
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
#print(gameWin)
#       gameWin = gameWinner(score1,score2)

