import random
import pyinputplus as pyip

#Random integer assigned for number guessing game
rand_int = random.randint(1, 20)

#Opening statement
print("I'm thinking of a number between 1 and 20. You have 5 guesses.")

#For loop allows the user 5 guesses
for i in range(5):
    user_guess = pyip.inputInt('Guess the number. ')
    if user_guess == rand_int:
        print('You guessed correctly!')
        break
    else:
        print('Try again.')

#Closing statement, game over
print(f'The correct answer was {rand_int}. Game over...')