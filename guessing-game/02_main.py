# Portfolio Project #2: Guessing Game with Scoring

# What it does: Computer picks random number, user guesses, gets hints, score calculated

# How it works:

# Computer picks random number (1-100)
# Initialize: guess counter = 0, timer starts
# Loop while user hasn't guessed correctly:
# Get user's guess
# Increase guess counter
# If guess too low → print "Too low"
# If guess too high → print "Too high"
# If guess correct → exit loop, show congrats message
# Calculate score based on:
# Number of guesses (fewer guesses = more points)
# Time taken (less time = more points)
# Efficiency bonus (if guessed in ≤ 5 tries)
# Save best score to file
# Ask if user wants to play again

# Logic for scoring:

# Base score: 1000 - (50 × number of guesses)
# Time bonus: 500 - (5 × seconds elapsed)
# Efficiency bonus: Extra points if guessed in ≤5 tries

# Key Concepts:

# random.randint() for random numbers
# File I/O (read/write high scores)
# time.time() for tracking seconds
# Scoring algorithms
# While loops with game logic

import random
import time

play1 = True
play2 = True
guess_counter = 0

while play1 == True:
    print("Computer is Guessing...")
    time.sleep(1)
    ran = random.randint(1, 100)
    print(ran)
    print("Your's Turn Now...")

    start = time.time()

    while play2 == True:
        user = int(input("Enter your guess: "))
        if(user == ran):
            print("Congrats you've guessed right!")
            play2 = False
        elif(user > ran):
            print("High, no. is Lesser!")
        elif(user < ran):
            print("Low, no. is Greater!")
        guess_counter += 1

    end = time.time()
    duration = end - start
    print(f"Time taken in guessing: {duration:.2f}")
    print(f"No. of Guesses: {guess_counter}")

    Base_score = max(0, 1000 - (50 * guess_counter))
    Time_bonus = max(0, 500 - (5 * duration))
    Total_score = Base_score + Time_bonus
    if guess_counter <= 5:
        Total_score += 100

    print(f"Your total score: {Total_score:.2f}")

    choice = input("Do you want to play another round(y/n): ")
    if (choice == "y"):
        play2 = True
        guess_counter = 0
    else:
        print("Exiting Loop...")
        play1 = False


