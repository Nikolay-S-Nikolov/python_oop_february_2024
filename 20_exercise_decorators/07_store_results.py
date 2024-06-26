def store_result(func):
    file_name = "results.txt"

    def wrapper(*args):
        with open(file_name, 'a') as store_file:
            store_file.write(f"Function {func.__name__} was called. Result: {func(*args)}\n")

    return wrapper


class store_results:
    _file_name = "results.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open(store_results._file_name, 'a') as store_file:
            store_file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args)}\n")


class store_results_with_param:
    _file_name = "results.txt"

    def __init__(self, param):
        self.param = param

    def __call__(self, func):
        def wrapper(*args):
            with open(store_results_with_param._file_name, 'a') as store_file:
                store_file.write(
                    f"Function {func.__name__} was called. Result: {func(*args)}. With param {self.param}\n")

        return wrapper


@store_results_with_param(2)
def add(a, b):
    return a + b


@store_results_with_param(3)
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
