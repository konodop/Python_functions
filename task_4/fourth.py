items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]
items_dict = {}

print(items, "\n")

for elem in items:
    product, typ = elem

    if typ not in items_dict.keys():
        items_dict[typ] = [product]
    else:
        items_dict[typ].append(product)

print(items_dict)
