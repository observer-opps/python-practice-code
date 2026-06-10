num = int(input("Enter a number: "))
n = []
for i in range(1, num+1):
    if num % i == 0:
        n.append(i)
print(f"Factors of {num} are {n}")