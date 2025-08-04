numbers = []

for i in range(99):
    task = input("Enter Yor Number: ")
    if task.lower()=="exit":
        break
    numbers.append(task)
print(numbers)
