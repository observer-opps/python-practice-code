import random
randomNum = random.randint(1, 100)
tries = 0

while True:
    num = int(input("Your guess: "))
    tries += 1

    if randomNum == num:
        print(f"Congratulations your guess is correct!. It took you {tries} tries.")
        break

    elif num > randomNum:
        print(f"Sorry, go a little lower")

    elif num < randomNum:
        print(f"Sorry, go a little higher")
