# Discussion 7

#### Question 1: Draw

The `draw` function takes a list `hand` and a list of unique non-negative integers `positions` that are all less than the length of `hand`. It removes `hand[p]` for each `p` in `positions` and returns a list of those elements in the order they appeared in `hand` (not the order they appeared in `positions`).

Fill in each blank with one of these names: `list`, `map`, `filter`, `reverse`, `reversed`, `sort`, `sorted`, `append`, `insert`, `index`, `remove`, `pop`, `zip`, or `sum`. See the [built-in functions](https://docs.python.org/3/library/functions.html) and [list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) documentation for descriptions of what these do.

```python
def draw(hand, positions):
    """Remove and return the items at positions from hand.

    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    return list(reversed( [hand.pop(i) for i in reversed(sorted(positions))] ))
```

------

#### Question 2: Keyboard

**Overview:** A keyboard has a button for every letter of the alphabet. When a button is pressed, it outputs its letter by calling an `output` function (such as `print`). Whether that letter is uppercase or lowercase depends on how many times the *caps lock* key has been pressed.

**First**, implement the `Button` class, which takes a lowercase `letter` (a string) and a one-argument `output` function, such as `Button('c', print)`.

The `press` method of a `Button` calls its `output` attribute (a function) on its `letter` attribute: either uppercase if `caps_lock` has been pressed an odd number of times or lowercase otherwise. The `press` method also increments `pressed` and returns the key that was pressed. *Hint*: `'hi'.upper()` evaluates to `'HI'`.

```python
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class CapsLock:
    def __init__(self):
        self.pressed = 0

    def press(self):
        self.pressed += 1

class Button:
    """A button on a keyboard.

    >>> f = lambda c: print(c, end='')  # The end='' argument avoids going to a new line
    >>> k, e, y = Button('k', f), Button('e', f), Button('y', f)
    >>> s = e.press().press().press()
    eee
    >>> caps = Button.caps_lock
    >>> t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]
    keyEEKeyeYEE
    >>> u = Button('a', print).press().press().press()
    A
    A
    A
    """
    caps_lock = CapsLock()

    def __init__(self, letter, output):
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0

    def press(self):
        """Call output on letter (maybe uppercased), then return the button that was pressed."""
        self.pressed += 1
        "*** YOUR CODE HERE ***"
        if Button.caps_lock.pressed % 2 == 1:
			self.output(self.letter.upper())
        else:
			self.output(self.letter)
        return self
```

**Second**, implement the `Keyboard` class. A `Keyboard` has a dictionary called `keys` containing a `Button` (with its `letter` as its key) for each letter in `LOWERCASE_LETTERS`. It also has a list of the letters `typed`, which may be a mix of uppercase and lowercase letters.

The `type` method takes a string `word` containing only lowercase letters. It invokes the `press` method of the `Button` in `keys` for each letter in `word`, which adds a letter (either lowercase or uppercase depending on `caps_lock`) to the `Keyboard`'s `typed` list. **Important:** Do not use `upper` or `letter` in your implementation of `type`; just call `press` instead.

```python
class Keyboard:
    """A keyboard.

    >>> Button.caps_lock.pressed = 0  # Reset the caps_lock key
    >>> bored = Keyboard()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o']
    >>> bored.keys['l'].pressed
    2

    >>> Button.caps_lock.press()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o', 'H', 'E', 'L', 'L', 'O']
    >>> bored.keys['l'].pressed
    4
    """
    def __init__(self):
        self.typed = []
        self.keys = {letter: Button(letter, self.typed.append) for letter in LOWERCASE_LETTERS} # Try a dictionary comprehension!

    def type(self, word):
        """Press the button for each letter in word."""
        assert all([w in LOWERCASE_LETTERS for w in word]), 'word must be all lowercase'
        "*** YOUR CODE HERE ***"
        for w in word:
            self.keys[w].press()
```

------

#### Question 3: Bear

Implement the `SleepyBear`, and `WinkingBear` classes so that calling their `print` method matches the doctests. Use as little code as possible and try not to repeat any logic from `Eye` or `Bear`. Each blank can be filled with just two short lines.

```python
class Eye:
    """An eye.

    >>> Eye().draw()
    '0'
    >>> print(Eye(False).draw(), Eye(True).draw())
    0 -
    """
    def __init__(self, closed=False):
        self.closed = closed

    def draw(self):
        if self.closed:
            return '-'
        else:
            return '0'

class Bear:
    """A bear.

    >>> Bear().print()
    ? 0o0?
    """
    def __init__(self):
        self.nose_and_mouth = 'o'

    def next_eye(self):
        return Eye()

    def print(self):
        left, right = self.next_eye(), self.next_eye()
        print('? ' + left.draw() + self.nose_and_mouth + right.draw() + '?')

class SleepyBear(Bear):
    """A bear with closed eyes.

    >>> SleepyBear().print()
    ? -o-?
    """
    "*** YOUR CODE HERE ***"
	def next_eye(self):
        return Eye(True)

class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ? -o0?
    """
    def __init__(self):
        "*** YOUR CODE HERE ***"
        self.nose_and_mouth = 'o'
        self.wink = False 

    def next_eye(self):
        "*** YOUR CODE HERE ***"
        self.wink = not self.wink
        return Eye(self.wink)
```

