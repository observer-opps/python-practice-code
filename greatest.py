lst = []
n = int(input("Enter number of elements in list: "))

for i in range (1, n+1):
    element = int(input(f"Enter element {i}: "))           # This block takes list as input
    lst.append(element)

greatest = lst[0]
index = 0

for j in range(len(lst)):
    if lst[j] > greatest:
        greatest = lst[j]
        index = j
        
print(f"Largest value is {greatest} at index {index}")
