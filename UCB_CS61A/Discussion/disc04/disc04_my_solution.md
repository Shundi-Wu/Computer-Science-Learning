# Discussion 4

#### Question 1: Insect Combinatorics

An insect is inside an `m` by `n` grid. The insect starts at the bottom-left corner `(1, 1)` and wants to end up at the top-right corner `(m, n)`. The insect can only move up or to the right. Write a function `paths` that takes the height and width of a grid and returns the number of paths the insect can take from the start to the end. (There is a [closed-form solution](https://en.wikipedia.org/wiki/Closed-form_expression) to this problem, but try to answer it with recursion.)

```python
def paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)
```

#### Question 2: Max Product

Implement `max_product`, which takes a list of numbers and returns the maximum product that can be formed by multiplying together non-consecutive elements of the list. Assume that all numbers in the input list are greater than or equal to 1.

```python
def max_products(s):
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    return max(s[0] * max_products(s[2:]), max_products(s[1:]))
```

#### Question 3: Sum Fun

Implement `sums(n, m)`, which takes a total `n` and maximum `m`. It returns a list of all lists:

1. that sum to `n`,
2. that contain only positive numbers up to `m`, and
3. in which no two adjacent numbers are the same.

Two lists with the same numbers in a different order should both be returned.

```python
def sum(n, m):
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []
        return sums_to_zero
    result = []
    for k in range(1, m + 1):
        result = result + [[k] + rest for rest in sums(n-k, m) if rest == [] or rest[0] != k]
    return result
```

