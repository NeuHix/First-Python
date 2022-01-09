import random

player = input("Your Turn: Stone(s) Paper(p) or Scissor(sc): ")

print("Comp Turn: Stone(s) Paper(p) or Scissor(sc): 'hidden'")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's' or 'stone'
elif randNo == 2:
    comp = 'p' or 'paper'
elif randNo == 3:
    comp = 'sc' or 'scissor'


def game_win(comp, player):
    if comp == player:
        return None
    elif comp == 's':
        if player == 'p':
            return True
        elif player == 'sc':
            return False
    elif comp == 'p':
        if player == 'sc':
            return True
        elif player == 's':
            return False
    elif comp == 'sc':
        if player == 's':
            return True
        elif player == 'p':
            return False


start = game_win(comp, player)
print(f"Computer Stroke: {comp}")
print(f"Your Stroke: {player}")
if start is None:
    print("Game is a Tie")
elif start:
    print("You Win!")
else:
    print("You Lose!")
