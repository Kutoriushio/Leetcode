class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) # Transform list into heap


    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val) #push the val onto the heap
        while len(self.nums) > self.k:
            heapq.heappop(self.nums) # pop the smallest item from heap
        return self.nums[0] # the top of the heap is the smallest item

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)