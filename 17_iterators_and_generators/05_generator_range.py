def genrange(start: int, end: int):
    # return (x for x in range(start, end + 1))
    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 10)))
