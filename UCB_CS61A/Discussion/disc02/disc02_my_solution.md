## Discussion 2

### Question 1:

What is the value of `result` after executing `result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)`?

**My Answer:** `result = 30`

### Question 2: Make Keeper

Implement `make_keeper`, which takes a positive integer `n` and returns a function `f` that takes as its argument another one-argument function `cond`. When `f` is called on `cond`, it prints out the integers from 1 to `n` (including `n`) for which `cond` returns a true value when called on each of those integers. Each integer is printed on a separate line.

```python
def make_keeper(n):
    def f(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)
        return True
    return f   
```

### Question 3: Digit Finder

Implement `find_digit`, which takes in a positive integer `k` and returns a function that takes in a positive integer `x` and returns the `k`th digit from the right of `x`. If `x` has fewer than `k` digits, it returns 0.

```python
def find_digit(k):
    def kth_digit(x):
        for i in range(1, k):
        	x = x // 10
        k_digit = x % 10
        return k_digit 
    return kth_digit
```

### Question 4: Match Maker

Implement `match_k`, which takes in an integer `k` and returns a function that takes in a variable `x` and returns `True` if all the digits in `x` that are `k` apart are the same.

```python
def match_k(k):
    def check(x):
		while x // (10 ** k) > 0:
			if (x % 10) != (x // (10 ** k)) % 10:
				return False
			x //= 10
		return True
	return check
```



### 	