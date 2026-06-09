num = int(input("Enter a number: "))
n = []
for i in range(1, num+1):
    if num % i == 0:
        n.append(i)

if len(n) == 2:
    print(f"{num} is a prime number")
else: 
    print(f"{num} is not a prime number")