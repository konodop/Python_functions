text = input().lower()

words = {}

for elem in text.split():
    word = words.get(elem)

    if not word:
        words[elem] = 1
    else:
        words.update({elem: word + 1})

top = (sorted(words.items(), key=lambda x: x[1], reverse=True))

top_5 = [item[0] for item in top[:5]]
print("Пять самых встречающихся слов:", *top_5)
