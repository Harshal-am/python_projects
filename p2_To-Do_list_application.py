def view_tasks():
    with open("task.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            print(task.strip())
def add_task(task):
    with open("task.txt", "a") as file:
        file.write(task + "")
        
def delete_task(task_number):
    with open("task.txt", "r") as file:
        tasks = file.readlines()
    with open("task.txt", "w") as file:    
        for i,task in enumerate(tasks):
            if i != task_number - 1:
                file.write(task)
            print(f"Task deleted sucessfully1")
                
print("1. view tasks")
print("2. add task")
print("3. delete task")

choice = input("enter choice (1/2/3): ")

if choice == '1':
    view_tasks()
elif choice == '2':
    task = input("enter task:")
    add_task(task)
elif choice == '3':
    view_tasks()
    task_number = int(input("enter task number to delete:"))
    
    delete_task(task_number)
    
else:
    print("Invalid choice")
