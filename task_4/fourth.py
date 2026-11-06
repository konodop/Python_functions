def factorial(n: int) -> str:
    """
    :param n: число до которого генерируются факториалы
    :return: выводит факториал от now
    """
    now = 0
    result = 1

    while now <= n:

        yield result

        now += 1
        result *= now


n = int(input())

gen = factorial(n)

for i in gen:
    print(i)
