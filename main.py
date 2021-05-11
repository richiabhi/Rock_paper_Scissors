import random
# Rock Paper Scissor
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


print("Computer's Turn : Rock(r) Paper(p) or Scissor(s) ?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
you = input("Your Turn : Choose Rock(r) Paper(p) or Scissor(s) : ")
res = gameWin(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if res == None:
    print("The game is a Tie !")
elif res:
    print("You won the game :) ")
else:
    print("You lose :( ")
