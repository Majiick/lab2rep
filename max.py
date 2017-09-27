from random import randint

arr = [randint(0, 100000) for _ in range(10000)]
print(max(arr))
