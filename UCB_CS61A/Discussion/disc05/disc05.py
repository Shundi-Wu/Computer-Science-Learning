def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def has_path(t, p):
    if len(p) == 1 and label(t) == p[0]:
        return True
    for b in branches(t):
        if has_path(b, p[1:]):
            return True
    return False

def find_path(t, x):
    if label(t) == x:
        return [x]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path

t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])