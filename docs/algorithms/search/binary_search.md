`binary search`
=

```
def binary_search(a: list, n: int) -> int:
    # инициализируем границы, индекс первого и индекс последнего элемента
    start, end = 0, len(a)
    while start <= end:
        mid = (start + end)//2
        guess = a[mid]
        if guess == n:
           return mid
        elif guess < n:
           start = mid + 1
        elif guess > n:
           end = mid - 1
    return -1
```
