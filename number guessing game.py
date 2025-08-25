#nunber gueesing game
import random
low_num = 1
high_num = 100
secret = random.randint(1, 100)
guesses = 0
print("Welcome to the number guessing game!")
while True:
    guess=input("Select a number btw 1 to 100: ")
    if not guess.isdigit():
        print(" Please enter a number")
        continue
        
    guess = int(guess)
    
    if guess == secret:
        print("Correct guess!")
        guesses += 1
        break
    elif guess > secret:
        print("Too high! try again")
        guesses += 1
    elif guess < secret:
        print("Too low! try again")
        guesses += 1
    elif guess > 100 or guess < 0 :
        print("invalid number, please select a number btw 1 to 100")
        guesses += 1
else:
    print("invalid guess, please select a number")
print(f"Number of attempts {guesses}")
        
        