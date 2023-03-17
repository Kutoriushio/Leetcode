# Solution(Python)

## Brute Solution TC(O(MN)) SC(O(1))

1. Enumerates each character in the original string as an "initiation point" and tries to match each time from the "initiation point" of the original string and the "first" of the matching string.

2. Successful match: return the original string's 'initiation point' for this match.

3. Failed match: enumerate the next "initiation point" of the original string and try the match again.
