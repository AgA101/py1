from typing import Generator

def pow_twelve(value: int) -> Generator:
    a0: int = 0
    a1: int = 1
    k: int = 0
    while k <= value:
        yield a0 + a1
        k += 1
        a0 = a1
        a1 = a0 + a1

for item in pow_twelve(int(input())):
    print(item)