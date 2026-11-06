import re


def find_abbr(s: str) -> list:
    abbr = re.findall(r'\b[А-ЯA-Z]{2,6}\b', s)
    return abbr


string = input()
res = find_abbr(string)

print(*res)
