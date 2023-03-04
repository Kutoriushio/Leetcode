class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.shuf = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        for i in range(len(self.shuf)):
            j = random.randrange(i, len(self.shuf))
            self.shuf[i], self.shuf[j] = self.shuf[j], self.shuf[i]
        return self.shuf


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()