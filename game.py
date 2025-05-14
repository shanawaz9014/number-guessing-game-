import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guess = None
    
    while guess != number_to_guess:
        guess = int(input("Make a guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

# Call the game
number_guessing_game()
