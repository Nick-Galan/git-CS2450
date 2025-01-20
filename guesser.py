import random
print("im going to guess your name")
name = input("what is your name?")
guesses = []
guessed = False
while(guessed == False):
    guess = random.randint(15, 30)
    if guess in guesses:
        continue:
    user_response = input("are you"+str(guess)+"years old?")
    if user_response == 'y' or user_response == 'Y':
        print(f"Haha! {name} is" + str(guess)+ "years old i guessed it!")
        guessed = True
    else:
        print("rats")
        