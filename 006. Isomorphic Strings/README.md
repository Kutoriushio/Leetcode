# Solution(python)

## Solution1:

1. Define a dictionary `dic_s_t` to map `s` to `t`, and another dictionary `dic_t_s` to map `t` to `s`.

2. Iterate over the two strings one character at a time.

3. (a) If `s[i]` not have a mapping in `dic_s_t` and `t[i]` not have a mapping in `dic_t_s`, add corresponding mappings

in both dictionaries.

3. (b) If either have a maaping in dictionary and the key-value pairs in the two dictionaries do not correspond, return False.

## Solution2:

Use set to remove duplicate elements in `s`, `t` and `zip(s,t)`, if they have different lengths, return False.
