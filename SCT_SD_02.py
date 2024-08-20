import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def check_guess(random_number, user_guess):
    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print(" Congratulations! You guessed the number!")

def play_game():
    random_number = generate_random_number()
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        user_guess = get_user_guess()
        check_guess(random_number, user_guess)
        if user_guess == random_number:
            break

def main():
    play_game()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()