import random
time_try = 0 
word = ['apple','world','ball','book','bag',"keyboard"]

random_chose = random.choice(word)
data1 = ["-"] *len(random_chose)
print(data1)
while time_try < 6:
    
    data2 = input("Enter Your Ges: ")
    if data2 in random_chose :
        for i in range(len(random_chose)):
            if random_chose[i] == data2:
                data1[i] = data2
                print(data1)
    else:
        time_try+=1
        print(f"The number of your mistakes: {time_try}/6")

    if time_try == 6:
        break
print(data1)
print("Answer:", random_chose) 