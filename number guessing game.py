import random as rd
lowest_num = int(input("Enter your lowest_number :"))
highest_num = int(input("Enter your highest_number :"))
answer = rd.randint(lowest_num, highest_num)
is_running = True
guesses = 0
print("A SIMPLE NUMBER GUESSING GAME")
print(f"Choose a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter the number you want to guess: ")

    # Check if the input is a number
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        # Check if the guess is within the range
        if guess < lowest_num or guess > highest_num:
            print("The number entered is out of range!")
            print(f"Choose a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Correct! The answer is {answer} and the number of guesses are {guesses}")
            is_running = False  # Stop the game after a correct guess
    else:
        print("Invalid guess! Please enter a valid number.")





