def even_parameters(func):
    def wrapper(*args):
        if next((arg for arg in args if not (isinstance(x, int) and x % 2 == 0)), False):
            return 'Please use only even numbers!'
        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


# Output
# 6
# Please use only even numbers!

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

# Output
# 384
# Please use only even numbers!
