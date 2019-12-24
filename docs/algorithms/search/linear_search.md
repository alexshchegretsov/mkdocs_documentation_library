`linear search`
=


```
def linear_search(a: list, n: int) -> int:
    for id, num in enumerate(a):
        if num == n:
            return id
    return -1


O(n)
Omega(1)
```
