import random

def roll(beginning, end):
	rollresult1 = random.randint(1,6)
	rollresult2 = random.randint(1,6)
	return rollresult1
	return rollresult2
def roundwinner(rollresult1, rollresult2):
	if rollresult1 > rollresult2:
		return player1
		print ("player1 wins the round")
	elif rollresult2 > rollresult1:
		return player2
		print ("player2 wins the round")
	elif rollresult1 == rollresult2:
		print ("This round was a draw")
def gamewinner(player1, player2):
	if player1 > player2:
		print ("player1 wins the game")
	elif player2 > player1:
		print ("player2 wins the game")


player1 = 0
player2 = 0
score1 = 0
score2 = 0
while player1 < 1 and player2 < 1:
	start = roll(1,6)
	start1 = roll(1,6)
	if start > start1:

	roundwinner = (1,6)
	if roundwinner == player1:
		player1 += 1
	elif roundwinner == player2:
		player2 += 1
	final = gamewinner (player1, player2)
print ("Final Results: ")

#final = gamewinner(player1, player2)
#print final
