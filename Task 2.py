import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    while not guessed_correctly:
        try:

            guess = int(input("Enter your guess (or type '0' to quit): "))


            if guess == 0:
                print("You decided to quit. The number was", number_to_guess)
                break

            attempts += 1


            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    guessing_game()
