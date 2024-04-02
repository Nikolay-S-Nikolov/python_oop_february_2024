def squares(n):
    x = 1
    while x <= n:
        yield x * x
        x += 1


print(list(squares(5)))
# var = [x * x for x in range(1, 6)]
# print(var)
