
import random

def play():

    user = input("whats your guess??? 'p' for paper,'r' for rock, 's' for scissors\n ")
    computer = random.choice(['p','r','s'])

    if user == computer:
        return 'It\'s a tie'
    # s>p , r>s,p>r
    if is_win(user,computer):
        return 'You Won!'
   
    return 'You lost!'
    
    
    
        
def is_win(player , opponent):
        # returns True if player wins 
        # s>p , r>s,p>r

    if (player =='r' and opponent == 's') or (player =='s' and opponent == 'p') \
              or (player == 'p' and opponent =='r'):
        return True



    

print(play())

