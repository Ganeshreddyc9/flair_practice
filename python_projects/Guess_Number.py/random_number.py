# guess the number 
#guessing game 

# where the computer has a secret number and we are guessing that seceret number 


import random 


# def guess(x):

#     random_number = random.randint(1,x)

#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'enter the numbers between 1 to {x}: '))
#         # print(guess)
#         if guess < random_number:
#             print("sorry,guess again, To low")
#         elif guess > random_number:
#             print('sorry, guess again, Too high')
    
#     print("Yay, congrats. you guessed the number {random_number} correctly!!")


# guess(10)


'''
#computer has to guess our secret number 
#so low and high is for to get the user feedback 
#for ex: our secret number is 7 
# and feedback is l they guessed 6 computer will check in that range from  1 - 6 only so we have to change the range
to 1-7 if we give low and high we can modify accordig to the users feedback 



here low and high varibale objects are used bcz based on computer guess we are gonna increase the value or decrease 
the value 

'''

def computer_guess(x):
    low = 1
    high = x
 
    feedback = ''

    while feedback != 'c' : 
        # low == high random.randint will throws an error 
        # so for that we can do 
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low

            feedback = input(f'is {guess} too high (H) too low (L) correct (C)??').lower()

        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay, computer guessed your number,{guess}, correctly!!")


computer_guess(200)