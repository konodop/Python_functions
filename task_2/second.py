def fib(need: int, a=1, b=0, now=1) -> int:
    """
    :param need: запрашиваемое число из ряда фибоначи
    :param a: первое число фибоначи используемое для вычисления
    :param b: второе число фибоначи используемое для вычисления
    :param now: длинна посчитанного ряда фибоначи
    :return: вывод запрашиваемого числа
    """
    if need == 0:
        return b
    elif need <= now:
        return a

    res = fib(need, a + b, a, now + 1)

    return res


inp = int(input())

otvet = fib(inp)

print(otvet)
