lst = [1, 3, 5, 7]

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        print("Your list is not sorted.")
        break
else: 
    print("Your list is sorted.")
