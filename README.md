# 8-10_does_countdown
8 Out of 10 Cats Does Countdown solver

![alt tag](https://cloud.githubusercontent.com/assets/284798/23587612/8c5fc00e-01b0-11e7-977c-808265bcd16e.png)

# Modifications

- Works with Python3
- Calculates with parts or parantheses, not just 'linear'
- Direct command line input option (in addition to the original input method)

```
python3 ./script.py 4 1 3 7 6 50 127
```

# Method

Like the original repository, the algorithm is simply to try at random different math manipulations with different randomized copies of the 6 input values.
Here, this sequence is divided at random into sub-sequences and calculated in two levels, mimicking calculations with parentheses.
The result is checked, and if closer to the target than earlier, the result is stored.

If at target, the result is shown.
The aglorithm continues searching for simpler expressions with exact match.
If no match is found, the best result is shown with a notification of how far away the result is from the target value.
Processing is stopped based on a number of seaches which didn't give any better result than already achieved.

# History

Forked from nicandris!
