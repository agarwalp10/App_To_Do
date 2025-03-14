# ---- Creating a To-Do List Application ----


# Create an empty list to start the progmra
your_tasks = []

print("\nWelcome to Pankaj To-Do Application")

# Functions will be created to Add tasks, Delete tasks, View tasks, and Exit application
def appMenu():
    print("\nMenu for your tasks:")
    print("add")
    print("view")
    print("delete")
    print("exit")


#function will prompt user to add a task to the list
def addTask(task_list): 
    # creating a loop so user can continue to add a task without going back to menu
    while True: 
        task = input("What task would you like to add (type 'back' to go back to menu): ")
        if task == "back":
            break

        else:
            task_list.append(task)
            print("Task addded!")
    
    return task_list

#function to view task 
def viewTask(task_list):
    # if there is no task, let user know and what their options are
    if not task_list:
        print("No tasks in list, please add or exit.")
    else: 
        print(f'Your To-Do List: {task_list}')
        for i, task in enumerate(task_list,1):
            print(f"{i}. {task}")

# function allows user to delete a task based on its task number
def deleteTask(task_list):
    viewTask(task_list)

    if task_list:
        try: 
            idx = int(input("Enter task number to delete: "))-1
            # if index is not between 0 and length then there is an error
            if 0 <= idx < len(task_list):
                rem_task = task_list.pop(idx)
                print(f"Task '{rem_task}' deleted")
            else: 
                print("Invaled number")
        except ValueError:
            print("Invalid input, try again")
        else: 
            viewTask(task_list)

    return task_list

# function to exit the program
def exitTask(task_list):
    print(f'Your To-Do List: {task_list}')
    print("You have now exited your To-Do list")

# function to run the application and calling all other functions 
def main():
    your_tasks = []
    while True:
        appMenu()
        choice = input("what would you like to do: ")
        if choice.lower() == "add":
            addTask(your_tasks)
        elif choice.lower() == "view":
            viewTask(your_tasks)
        elif choice.lower() == "delete":
            deleteTask(your_tasks)
        elif choice.lower() == "exit":
            exitTask(your_tasks)
            break
        else: 
            print("Invalid input, try again!")

main()




