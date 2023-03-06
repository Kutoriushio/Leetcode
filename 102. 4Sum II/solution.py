class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        res = 0
        dic = {}
        for i in range(n):
            for j in range(n):
                s = nums1[i] + nums2[j]
                dic[s] = dic.get(s, 0) + 1
        for i in range(n):
            for j in range(n):
                s = nums3[i] + nums4[j]
                if -s in dic:
                    res += dic[-s]
        return res