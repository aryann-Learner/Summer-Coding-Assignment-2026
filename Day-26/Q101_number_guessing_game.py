# Q101 - Number guessing game
import random
secret = random.randint(1, 100)
print("Guess a number between 1 and 100")
while True:
    guess = int(input("Your guess: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You guessed it!")
        break