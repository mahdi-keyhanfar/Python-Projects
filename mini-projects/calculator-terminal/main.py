data1 = float(input("Enter Your Number: "))
data2 = input("Select (+,-,*,/)")
data3 = float(input("Enter Your Number2 : "))

if data2 == "+":
    print(f"The sum of your numbers ==> {data1+data3}")
elif data2 == "-":
    print(f"The minus of your numbers ==> {data1-data3}")
elif data2 == "*":
    print(f"The times of your numbers ==> {data1*data3}")
elif data2 == "/":
    print(f"The divided of your numbers ==> {data1/data3}")
else:
    print("Invalid Input")