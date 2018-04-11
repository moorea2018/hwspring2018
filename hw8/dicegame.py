import random

player1 = 0
player2 = 0

while player1 < 2 and  player2 < 2:
	roll1 = random.randint(1,6)
	roll2 = random.randint(1,6)
	if roll1 > roll2:
		print ("player1 wins the round")
		player1 += 1
	elif roll2 > roll1: 
		print ("player2 wins the round")
		player2 += 1
	elif roll1 == roll2:
		print ("this round was a draw")

print ("Final Result: ")
print (player1, player2)
if player1 > player2:
	print("player1 wins the match")
elif player2 > player1:
	print("player2 wins the match")
