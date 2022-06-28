import random

player1_score = 0
player2_score = 0
 
player1 = input("enter player 1 name: ")
player2 = input("enter player 2 name: ")

for i in range(1,19):
    run= random.randint(0,6)
    print(run,end=" ")
    player1_score+= run
    input()

print(f"{player1} scor: {player1_score}")

for i in range(1,19):
    run=random.randint(0,6)
    print(run,end=" ")
    player2_score+= run
    input()

print(f"{player2} scor: {player2_score}")

if player1_score>player2_score:
    print(f"{player1} won the game !!! ")
elif player1_score<player2_score:
    print(f"{player2} won the match !!! ")
else:
    print("TIE !!!")