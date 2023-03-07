# Solution(Python)

## Solution1 TC(O(2N)) SC(O(min(m, n)))

1. Use HashSet to store the characters in current window `[i,j)` (`j=i` initially). 

2. Slide the index `j` to the right. If it is not in the HashSet, we slide `j` further. 

3. Doing so until `s[j]` is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index `i`. 

4. If we do this for all `i`, we get our answer.

## Solution1 TC(O(N)) SC(O(min(m, n)))

1. Skip all the elements in the range `[i,j]`and let `i` to be `j+1` directly.
