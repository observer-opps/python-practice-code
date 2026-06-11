num = int(input("Enter a number: "))
rev = 0
num1 = num
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

if num1 == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
