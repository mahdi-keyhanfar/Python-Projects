import random
counter_gusess = 0
guess_number = 0
choice = random.randint(1,10)

while guess_number != choice:
    guess_number = int(input("Gusses a number: "))
    if guess_number == choice:
        print("You win 🏆")
    else:
        counter_gusess += 1
        print(f"Try again🥱 \nThe number of gusses:{counter_gusess}")