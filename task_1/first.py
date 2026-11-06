def f(s: str, was: str = "") -> str:
    """
    :param s: строка со скобками для проверки
    :param was: строка открытых, но ещё не закрытых скобок
    :return: возвращает верность скобок
    """

    if not s:
        if was:
            return "Неправильно"
        return "Правильно"

    if s[0] in "([{":
        was += s[0]

    else:
        if s[0] == ")":
            if was and was[-1] == "(":
                was = was[:-1]
            else:
                return "Неправильно"

        elif s[0] == "]":
            if was and was[-1] == "[":
                was = was[:-1]
            else:
                return "Неправильно"

        elif s[0] == "}":
            if was and was[-1] == "{":
                was = was[:-1]
            else:
                return "Неправильно"

    result = f(s[1:], was)

    return result


s = input()

for i in set(s):
    if i not in "[{()}]":
        s = s.replace(i, "")

res = f(s)

print(res)
