# Discussion 6

#### Question 1: Big Fib

Complete the expression below by writing only names and parentheses in the blanks so that it evaluates to the smallest Fibonacci number that is larger than 2024

```python
def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

next(filter(lambda n: n > 2024, gen_fib()))
```

------

#### Question 2: Something Different

Implement `differences`, a generator function that takes `t`, a non-empty iterator over numbers. It yields the differences between each pair of adjacent values from `t`. If `t` iterates over a positive finite number of values `n`, then `differences` should yield `n-1` times.

```python
def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    previous_x = next(t)
    for x in t:
        yield x - previous_x
        previous_x = x    
```

------

#### Question 3: Partitions

Implement `partition_gen`, a generator functon that takes positive `n` and `m`. It yields the partitions of `n` using parts up to size `m` as strings.

```python
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n-m, m):
        yield p + '+' + str(m)
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n, m-1)
```

