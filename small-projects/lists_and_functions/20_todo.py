# Project 20: Simple To-Do List Manager

# What it does: Create, view, add tasks to a list
# Logic:

# Create empty list for tasks
# Create function to add task: gets task from user, appends to list
# Create function to show tasks: loops through list, prints each with number
# Test: add 2-3 tasks, then show all tasks

# Key Concepts: Functions, lists, enumerate()

def addtask(x):
    for i in range(1, x+1):
        t = input(f"Enter task {i}: ")
        tasks.append(t)
    return

def show():
    # enumerate(tasks, 1) loops through the list while automatically tracking the count.
    # The '1' sets the starting number to 1 (instead of default 0).
    # It returns two values each time: the current number (index) and the item (task).   
    for number,i in enumerate(tasks,1):
        print(f"{number}.{i}")

tasks = []
n = int(input("How many tasks do you want to add: "))
addtask(n)
show()