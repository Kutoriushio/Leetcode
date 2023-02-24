# Solution(Python)

## Negative Marking (TC(O(N)) SC(O(1)))

1. Iterate over the array, evaluating each element.

2. Since we use negative marking, we must ensure that the current element `cur` is positive.

3. Check if `nums[cur]` is negative.

4. If it is, then we have already performed this operation for the same number, and hence curcurcur is the duplicate number. Store `cur` as the duplicate and exit the loop.

5. Otherwise, flip the sign of `nums[cur]`(i.e. make it negative). Move to the next element and repeat step 3.

## Binary Search (TC(O(nlogN)) SC(O(1)))

1. Apply binary search and start with the entire range of numbers `[1,n]`.

2. Find the mid-point.

3. Count how many numbers in the input array are less than or equal to it.

4. Repeat step 3 until we've exhausted the search range and return the lowest value that met the aforementioned condition.

## Two pointers (TC(O(nlogN)) SC(O(1)))

1. Traverse list using two pointers.

2. Move one pointer(slow) by one and another pointer(fast) by two.

3. If these pointers meet at the same position then there is a loop.

4. When they meet in the circle, use another pointer starts from the head, and this pointer moves one step with the slow pointer, when they meet, this number is the entry.

