str = input("Enter a string of random characters: ")
digitCount = 0
letterCount = 0
symbolCount = 0

for i in str:
    if i.isdigit():
        digitCount += 1
    elif i.isalpha():
        letterCount += 1
    else:
        symbolCount += 1

print(f"Number of digits is {digitCount}, number of letters is {letterCount} and number of special symbols is {symbolCount}")
