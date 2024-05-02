import random

from words import words # from words--> this words is word.py and  from words varibale in the words.py assigned to the varibale check in the words.py file 
import string
# print(words)
# actually we have to keep chossing the word until we get a valid word that we can guess in hangman

def get_valid_word(words):


    word = random.choice(words) # randomly chosses something from the list 
    # print(word,".....")
    while '_' in word or " " in word: #
        word = random.choice(words)

    # print(word)
    # return word
    return word.upper()

 

# we need to be able to keep track of which letters wev'e guess  and which letters in the word we've correctly guessed 
# and we also need to track what is a valid letter and what is it 
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed


    lives = 6

    # getting user input 
    while len(word_letters) > 0 and lives > 0:

        # letters used 
        # ' '.join(['a','b','cd'])--> 'a b cd' 
        print('you have ',lives ,"lives left you have used these letters",' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current Word: ', " ".join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1


        elif user_letter in used_letters:
            print('you have already used that character.please try again')
        else:
            print('invalid characters.please try again')
         

    # gets here when len(words_letters)== 0 or when lives == 0
            
    if lives == 0:
        print('you died.,sorry.The word was', word)
    else:
        print('You guessed the word', word,'!!!')

# user_input = input('type something: ')

# print(user_input)






hangman()

# get_valid_word(words)

