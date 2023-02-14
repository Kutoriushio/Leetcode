# Solution(Python)

## TC(O(logN)) SC(O(1))

If you go in the downhill direction, you might encounter a new peak, but maybe it's a slope that keeps descending and ends up at the boundary. But if you go in the uphill direction, even if you end up on the boundary all the way up, since the most boundary is negative infinity, you will definitely find the peak. In a nutshell, going in the increasing direction, dichotomous, you will definitely find it, going in the decreasing direction you just might find it, or maybe not.
