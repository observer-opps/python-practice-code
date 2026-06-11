# Find the mean (average) of all list elements.
lst = []
n = int(input("Enter number of elements in list: "))

for i in range (1, n+1):
    element = int(input(f"Enter element {i}: "))
    lst.append(element)

sum = sum(lst)
mean = sum/n
print(f"Mean of elements is {mean}")
