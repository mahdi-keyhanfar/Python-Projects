numbers = []
while True:

    entry = input("""
1-Add Task
2-Edit Task    
3-Delete Task
4-View all tasks
5-Exit
Select your option:
""")
    if entry=="1" or entry.lower()== "add task" :

        for i in range(99):
            task = input("Enter Yor Task: ")
            if task.lower()=="exit":
                break
            numbers.append(task)

        for task,value in enumerate(numbers,start=1):
            print(f"{task}.{value}")

    elif entry=="2" or entry.lower()== "edit task" :
        if len(numbers) == 0:
            print("No Task To Edit!")
        else:
            for task,value in enumerate(numbers,start=1):
                print(f"{task}.{value}")

            task_num = (input("Enter Your Task Number: "))
            if task_num.isnumeric():
                task_num = int(task_num)
                if task_num>=1 and task_num<=4 :
                    new_task = input("Enter Your New Task")
                    numbers[task_num - 1 ] = new_task 
                    print("Task updated.")        
                else:
                    print("Task number must be between 1 and 5")
            else:
                print("Unvalid Input")


    elif entry=="3" or entry.lower()== "delete task" :
        pass
