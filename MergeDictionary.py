d1 = {"a": 1}
d2 = {"b": 2}
# d1.update(d2)
# print(d1)

for i in d2:
    d1[i] = d2[i]
print(d1)