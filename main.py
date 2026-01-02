# To - Do List Manager

list1= [] # global variable
def add_task():
    while True:
        x = input("Enter task or enter 'done' to exit: ") # local variable
        if x== 'done':
            print("All tasks entered successfully.")
            break
        else:
            list1.append(x)
    global y
    
    y = dict.fromkeys(list1,False)

def updating_tasks(y):
    while True:
        x = input("Enter task that is completed or enter 'done' to exit: ") # local variable
        if x == 'done':
            print("All tasks entered successfully.")
            break
        elif x in y:
            y[x] = True
        else:
            print("Task not found.")
    for key,value in y.items():
            print (key, value)

def delete_task(y):
    while True:
        x = input("Enter task to be deleted or enter 'done' to exit: ") # local variable
        if x == 'done':
            print("All tasks entered successfully.")
            break
        elif x in y:
            y.pop(x,None)
    

# Menu Driven Program           
while True:
    print("""
          ... Welcome to Task Manager ...
          Enter 1 for adding task
          Enter 2 for Viewing Task
          Enter 3 for updating status
          Enter 4 for deleting task
          Enter 5 for exit        
    """)

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_task()
    elif ch == 2 :
        print("Tasks")
        for key,value in y.items():
            print (key, value) 
    elif ch == 3:
        updating_tasks(y)
    elif ch == 4:
        delete_task(y)
    elif ch == 5:
        break

    else:
        print("Invalid choice")