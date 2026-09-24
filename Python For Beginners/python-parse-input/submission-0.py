from typing import List

def read_integers() -> List[int]:
    number = input()
    return [int(x) for x in number.split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
