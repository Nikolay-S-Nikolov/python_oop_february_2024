from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, el: str) -> None:
        self.data.append(el)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self):
        result = [self.data[idx] for idx in range(len(self.data) - 1, -1, -1)]
        return f'[{", ".join(result)}]'

s = Stack()
s.push('1')
s.push('2')
s.push('3')
s.push('4')
print(s)

