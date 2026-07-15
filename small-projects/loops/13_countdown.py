# Project 13: Countdown Timer

# What it does: Counts down from a number to 1, prints each second
# Logic:

# Get number of seconds from user
# Loop from that number down to 1
# Each loop: print number, pause 1 second (using time module)
# When done: print "Time's up!"

# Key Concepts: for loops with negative step, time.sleep(), import

import time

seconds = int(input("Enter the number of seconds to count down: "))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1) # Tells the computer to wait exactly one second before running the next loop

print("Time's up!")