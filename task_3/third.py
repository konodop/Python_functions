list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

print("list1:", list1, "\nlist2:", list2, "\n")

both = []
uniq_1 = []
uniq_2 = []

for i in list1:
    if i in list2:
        both.append(i)
    else:
        uniq_1.append(i)

for i in list2:
    if i not in list1:
        uniq_2.append(i)

print("Общие:", *both)
print("Уникальны для первого:", *uniq_1)
print("Уникальны для второго:", *uniq_2)
