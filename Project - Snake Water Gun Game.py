import random

player = input("Your Turn: Snake(s) Water(w) or Gun(g): ")

randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
print("Comp Turn: Snake(s) Water(w) or Gun(g):", comp)


def gamewin(comp, player):
    if comp == player:
        return None
    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True
    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True


start = gamewin(comp, player)

if start is None:
    print(" \n \tGame is a Tie")
elif start:
    print(" \n \tYou Win!")
else:
    print(" \n \tYou Lose!")
