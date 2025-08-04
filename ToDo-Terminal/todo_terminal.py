numbers = []

entry = input("""
Select your option: 
1-Add Task
2-Edit Task
3-Delete Task
4-Exit
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
    pass
    
    
elif entry=="3" or entry.lower()== "delete task" :
    pass
