# Solution(Python)

## Solution1 (TC(O(N^3)) SC(O(1)))

1. considers each number in `nums`, attempting to count as high as possible from that number using only numbers in `nums`.

## Solution2 (TC(O(NlogN)) SC(O(1)))

1. Sort the `nums`.

2.  If the current number and the previous are equal, then our current sequence is neither extended nor broken, so we simply move on to the next number. If they are unequal, then we must check whether the current number extends the sequence.

## Solution3 (TC(O(N)) SC(O(1)))

1. We only attempt to build sequences from numbers that are not already part of a longer sequence. This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.