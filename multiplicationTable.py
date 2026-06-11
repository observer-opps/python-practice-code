num1 = int(input("Enter a number: "))
num2 = 1

for i in range (num1, (num1*10) + 1, num1):
    print(f"{num1} x {num2} = {i}")
    num2 += 1