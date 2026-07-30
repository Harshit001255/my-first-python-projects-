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
                line = task
                parts = line.split("] ")
                status_part = parts[0].strip("[") #remove [ bracket from the start
                task_part = parts[1]
                tasks.append({"task": task_part, "status": status_part})


choice = True
while choice == True:
    print("1. View All Tasks\n2. Add Task\n3. Delete Task\n4. Mark Complete\n5. Clear Completed\n6. Statistics\n7. Save & Exit")
    try:
        option = int(input("Enter your Choice: "))
    except ValueError:
        print("Enter a number(1-7)!")
        continue
    match option:
        case 1:
            for index, task in enumerate(tasks):
                print(f"{index+1}.{"[" + task["status"] + "]" + " " + task["task"] }")

        case 2:
            will = True
            while will == True:
                add_task = input("Enter tasks: ")
                if add_task == "":
                    print("Enter valid task...")
                elif add_task.lower() == "no":
                    will = False
                    break
                else:
                    tasks.append({"task": add_task, "status": "TODO"})

        case 3:
            try:
                remove_task = int(input("Enter the no. of task to Delete: "))
                if remove_task < 1 or remove_task > len(tasks):
                    print("Invalid task number!")
                else:
                    tasks.pop(remove_task - 1)
            except ValueError:
                print("Enter a number...")
            except IndexError:
                print("Invalid task number...")

        case 4:
            try:
                task_choice = int(input("Which task number to mark complete? "))
                if task_choice < 1 or task_choice > len(tasks):
                    print("Error!")
                else:
                    for index, task in enumerate(tasks):
                        if index == task_choice - 1:
                            tasks[index]["status"] = "DONE"
                            print("Done")
                            break
            except ValueError:
                print("Enter a number!")

        case 5:
            new_tasks = []
            for task in tasks:
                if task["status"] == "TODO":
                    new_tasks.append(task)

            tasks = new_tasks
            print("Cleared all completed tasks!")

        case 6:
            total_count = 0
            completed_count = 0

            for task in tasks:
                total_count += 1
                if task["status"] == "DONE":
                    completed_count += 1

            remaining_count = total_count - completed_count
            if total_count == 0:
                percentage = 0
            else:
                percentage = (completed_count/total_count)*100
            if total_count == 0:
                filled_blocks = 0
                empty_blocks = 10
            else:
                filled_blocks = int((completed_count/total_count)*10)
                empty_blocks = int(10 - filled_blocks)

            print(f"Total tasks: {total_count}\nCompleted: {completed_count}\nRemaining: {remaining_count}\nPercentage: {percentage:.2f}")
            print("█"*filled_blocks + "░"*empty_blocks )

        case 7:
            try:
                f = open("todo-app/list.txt", "w")
                for task in tasks:
                    f.write("[" + task["status"] + "]" + " " + task["task"] + "\n")
                f.close()

                choice = False
                print("Saved Successfully...")
                print("Exiting loop...")
            except Exception:
                print("Error: Could not save file")


        case _:
            print("Enter 1-7 only!")