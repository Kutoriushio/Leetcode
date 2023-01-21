# Solution(Python)

1. If the length of `s` is odd, return `False`.

2. Use a dictionary to store a pair of brackets.

3. Iterate over `s` , place the open brackets on top of the stack, if meet the same type closed brackets, pop it out.

4. After iteration, if there is no brackets in stack, return `True`