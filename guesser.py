import random

print("I'm going to guess your age.")

name = input("What is your name? ")
guesses = []
guessed = False

while not guessed:
    guess = random.randint(15, 30)
    
    if guess in guesses:
        continue
    
    guesses.append(guess)
    
    user_response = input(f"Are you {guess} years old? (y/n): ")
    
    if user_response.lower() == 'y':
        print(f"Haha! {name} is {guess} years old. I guessed it!")
        guessed = True
    else:
        print("Rats, I guessed wrong!")
