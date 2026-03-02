import random

print ('Welcome to the Number Guessing Game!')

while True:
    number_of_guesses = 0
    secret_number = random.randint(1, 100)
    print ('To start type in a number between 1 - 100. To end the game type "0"')
    while True:
        guess = int(input())
        number_of_guesses += 1
        if guess == 0:
            break
        if guess == secret_number and number_of_guesses != 1:
            print (f'Good job, you guessed the correct number! It only took {number_of_guesses} tries.\n')
            break
        if guess == secret_number and number_of_guesses == 1:
            print ('Wow, first try! You are so lucky.\n')
            break
        if guess > secret_number:
            print ('Lower')
        if guess < secret_number:
            print ('Higher')
    if guess == 0:
        break
print ('See you latter!')
