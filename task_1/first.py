def f(s) -> str:
    if not s:
        return "Правильно"

    if (s[0] == "(" and s[-1] == ")" or s[0] == "["
            and s[-1] == "]" or s[0] == "{" and s[-1] != "}"):

        return f(s[1:-1])

    else:
        return "Неправильно"


s = input()

for i in set(s):
    if i not in "[{()}]":
        s = s.replace(i, "")

print(f(s))
