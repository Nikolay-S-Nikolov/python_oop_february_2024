from typing import List
from math import sqrt


def get_primes(nums: List[int]):
    for num in nums:
        if num < 2:
            continue
        for divisor in range(2, int(sqrt(num)) + 1):
            if not num % divisor:
                break
        else:
            yield num


print(list(get_primes(list(range(2, 100)))))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
