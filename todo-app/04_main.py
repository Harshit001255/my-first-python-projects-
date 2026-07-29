# Portfolio Project #4: To-Do List Manager with File Save

# What it does: Create tasks, mark complete, delete, save to file, load on startup

# How it works:

# On startup: Load tasks from file (if exists)
# Show menu in loop:
# View all tasks (show with number, status)
# Add task (ask for task, add to list)
# Mark complete (ask which task number, change status)
# Delete task (ask which task number, remove from list)
# Clear completed (remove all completed tasks)
# Show statistics (count total, completed, remaining)
# Save and exit
# When user quits: Save all tasks to file

# Task representation:

# Each task is a string with status: "[TODO] Task name" or "[DONE] Task name"
# Or use list of dictionaries with status and description

# File operations:

# Load: Read file line by line, create list
# Save: Write each task as new line

# Statistics:

# Count total tasks
# Count completed tasks
# Calculate percentage complete
# Show progress bar (visual with █ and ░)

# Key Concepts:

# File I/O (read/write)
# List manipulation (add, remove, modify)
# String operations
# Loops and conditionals
# Data persistence

try:
    f = open("todo-app/list.txt", "r")
    content = f.read()
    f.close()
except FileNotFoundError:
    content = ""
    tasks = []
else:
    if content == "":
        tasks = []
    else:
        list = content.split("\n")
        tasks = []
        for task in list:
            if task != "":
                tasks.append({"task": task, "status": "TODO"})


print("1. View All Tasks\n2. Add Task\n3. Delete Task\n4. Save & Exit")

choice = True
while choice == True:
    try:
        option = int(input("Enter your Choice: "))
    except ValueError:
        print("Enter a number(1-4)!")
        continue
    match option:
        case 1:
            for index, task in enumerate(tasks):
                print(f"{index+1}.{task['task']}")

        case 2:
            will = True
            while will == True:
                add_task = input("Enter tasks: ")
                if add_task.lower() == "no":
                    will = False
                else:
                    tasks.append({"task": add_task, "status": "TODO"})

        case 3:
            try:
                remove_task = int(input("Enter the no. of task to Delete: "))
                tasks.pop(remove_task - 1)
            except ValueError:
                print("Enter a number...")
            except IndexError:
                print("Invalid task number...")

        case 4:
            f = open("todo-app/list.txt", "w")
            for task in tasks:
                f.write(task["task"] + "\n")
            f.close()

            choice = False
            print("Exiting loop...")

        case _:
            print("Enter 1-4 only!")