# Discussion 3

#### Question 1: Swipe

Implement `swipe`, which prints the digits of argument `n`, one per line, first backward then forward. The left-most digit is printed only once. Do not use `while` or `for` or `str`. (Use recursion, of course!)

```python
def swipe(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)
```

#### Question 2: Skip Factorial

Define the base case for the `skip_factorial` function, which returns the product of every other positive integer, starting with `n`.

```python
def skip_factorial(n):
	if n <= 2:
        return n
    else:
        return n * skip_factorial(n-2)
```

#### Question 3: Is Prime

Implement `is_prime` that takes an integer `n` greater than 1. It returns `True` if `n` is a prime number and `False` otherwise. Try following the approach below, but implement it recursively without using a `while` (or `for`) statement.

```python
def is_prime(n):
    def check_all(i):
        "Check whether no number from i up to n evenly divides n."
        if i == n: 
            return True
        elif n % i == 0:
            return False
        return check_all(i + 1)
    return check_all(2)
```

#### Question 4: Recursive Hailstone

Recall the `hailstone` function from [Homework 1](https://cs61a.org/hw/hw01/). First, pick a positive integer `n` as the start. If `n` is even, divide it by 2. If `n` is odd, multiply it by 3 and add 1. Repeat this process until `n` is 1. Complete this recursive version of `hailstone` that prints out the values of the sequence and returns the number of steps.

```python
steps = 0
def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)
```

#### Question 5: Sevens

Implement `sevens` which takes a positive integer `n` and a number of players `k`. It returns which of the `k` players says `n`. You may call `has_seven`.

An effective approach to this problem is to simulate the game, stopping on turn `n`. The implementation must keep track of the final number `n`, the current number `i`, the player `who` will say `i`, and the current `direction` that determines the next player (either increasing or decreasing). It works well to use integers to represent all of these, with `direction` switching between `1` (increase) and `-1` (decreasing).

```python
def has_seven(n):
    if n > 0 and n % 7 == 0:
        return True
    if n == 0:
        return False
    if n % 10 == 7:
        return True
    else:
    	return has_seven(n // 10)

def sevens(n, k):
    def f(i, who, direction):
        if i == n:
            return who
        if has_seven(i):
            direction = -direction
        if who + direction == 0:
            who = k - direction
        if who + direction == k + 1:
            who = 1 - direction
        return f(i+1, who + direction, direction)
    return f(1, 1, 1)
```

