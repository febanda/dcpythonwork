import random

my_random_number = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')
count = 5


while True:
    number = input('What is the number?')
    if number == my_random_number:
        print('Yes! You win!')
        play_again = input('Do you want to play again (Y or N)?')
        break
    elif number < my_random_number:
        print(str(number) + ' is too low.')
        count -= 1
        print('You have ' + str(count) + ' guesses left')
    elif number > my_random_number:
        print(str(number) +  ' is too high.')
        count -= 1
        print('You have ' + str(count) + ' guesses left')
    else:
        print('You ran out of guesses!')
        play_again = input('Do you want to play again (Y or N)?')
        
    
        
        