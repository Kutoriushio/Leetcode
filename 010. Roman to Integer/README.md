# Solution(Python):

## Solution 1:

1. Use `IIII`, `VIIII`, `XXXX`, `LXXXX`, `CCCC`, `DCCCC` to replace `IV`, `IX`, `XL`, `XC`, `CD`, `CM` respectively.

2. Iterate over the string `s`.


## Solution 2:

1. Iterate over the string `s` from right to left, record the largest number in the iteration.

2. If next number is bigger than recorded number, then plus it and update the largest number.

3. If not, minus it.