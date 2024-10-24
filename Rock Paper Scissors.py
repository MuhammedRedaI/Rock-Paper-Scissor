import random

def game():

    player = input("what is your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors \n").lower()
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return "it's a Tie!"
    if is_win(player, computer):
        return "Congrats, You won!"
    return "you Lost :( "

def is_win(pl,com):
    #r > s, P > r, s > p 
    if pl == 'r' and com == 's' or pl == 'p' and com == 'r' or pl == 's' and com == 'p':
        return True
    return False

    
print(game())