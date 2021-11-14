import random as r
from replit import clear

words = ['wajid','abhinavan','likith','janakisai']


random_word = r.choice(words)
gameover = False
answer_to_be_guessed = ''
lives = 6
user_guess = ''
hangman_logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

'''
hangman = [
    '''
     _______
     |/      
     |      
     |      
     |       
     |      
     |
 ____|___
''',
'''
     _______
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|___
''',
'''
     _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 ____|___
''',
'''
     _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ____|___
''',
'''
     _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 ____|___
''',
'''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___
''',
'''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 ____|___
'''





]
# adding underscores to answer_to_be_guessed
for i in range(len(random_word)):
    answer_to_be_guessed += '_'

# hangman logo
print(hangman_logo)

# letting user know the no of letters to be guessed
print(f"You have to Guess {len(random_word)} no of letters, Lives remaining = {lives}")
# game engine
while not gameover:
    # print(random_word)
    print(hangman[6-lives])
    #printing the answer_to_be_guessed to be guessed 
    print(answer_to_be_guessed)
    character = input("\n enter  your guess : ").lower()
    clear()
    if character in answer_to_be_guessed:
        print(f"You've already Guessed {character}, try another letter")
        pass
    
    if character in random_word:
        for i in range(len(random_word)):
            if character == random_word[i]:
                answer_to_be_guessed = answer_to_be_guessed[:i] + character + answer_to_be_guessed[i + 1:]
    else:
        lives -= 1
        print(f"You Guessed the letter {character}, Thats not the correct letter you lost a life \n {lives} remaining")
    
    user_guess += character
    if not '_' in answer_to_be_guessed:
        print("You Won The Game You Saved A life You Are A Hero")
        gameover = True
    elif lives == 0:
        print(f"The answer  was {random_word},\nYou Couldn't Save Any Life You Lost The Game")
        gameover = True

     
    