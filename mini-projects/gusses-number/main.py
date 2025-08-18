import random
counter_gusess = 0
guess_number = 0
choice = random.randint(1,10)

while guess_number != choice:
    guess_number = int(input("Gusses a number: "))
    if guess_number == choice:
        print("\033[92mYou win 🏆\033[0m")
    else:
        counter_gusess += 1
        print(f"Try again🥱 \n\033[91mThe number of gusses:{counter_gusess}\033[0m")