# Count the frequency of each element in a list using a dictionary.
lst = ["a","b","a","c","b","a"]
dict = {}


for i in lst:
    if i in dict.keys():
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

print(dict)
