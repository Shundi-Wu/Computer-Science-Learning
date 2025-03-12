# Discussion 5

#### Question 1: Warm Up

```python
t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])
result = label(min(branches(max([t1, t2], key=label)), key=label))
```

**Solution:** `result = 6`

------

#### Question 2: Has Path

Implement `has_path`, which takes a tree `t` and a list `p`. It returns whether there is a path from the root of `t` with labels `p`. For example, `t1` has a path from its root with labels `[3, 5, 6]` but not `[3, 4, 6]` or `[5, 6]`.

```python
def has_path(t, p):
    if len(p) == 1 and label(t) == p[0]:
        return True
    for b in branches(t):
        if has_path(b, p[1:]):
            return True
    return False
```

```python
def has_path(t, p):
    if p == [label(t)]:
        return True
    elif label(t) != p[0]:
        return False
    else:
        return any([has_path(b, p[1:]) for b in branches(t)]) 
```

------

#### Question 3: Find Path

Implement `find_path`, which takes a tree `t` with unique labels and a value `x`. It returns a list containing the labels of the nodes along a path from the root of `t` to a node labeled `x`.

If `x` is not a label in `t`, return `None`. Assume that the labels of `t` are unique.

```python
def find_path(t, x):
    if label(t) == x:
        return [x]
	for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path
```



