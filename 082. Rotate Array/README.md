# Solution(Python)

## Solution1 TC(O(N)) SC(O(N))

1. Create a copy of `nums`

2. Change the number of list by using equation `(i+k) % n`.

3. Copy the new array to the original one.

## Solution2 TC(O(N)) SC(O(1))

1. Reverse all the elements of the array.

2. Reversethe first `k` elements followed by reversing the rest `n-k` elements gives us the required result.