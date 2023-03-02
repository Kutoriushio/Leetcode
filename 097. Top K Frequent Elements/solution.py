class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        return heapq.nlargest(k, dic.keys(), key=dic.get)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        res = []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num, count in dic.items():
            bucket[count].append(num)
        index = n
        for i in range(n, -1, -1):
            if not bucket[i]:
                continue
            for num in bucket[i]:
                if len(res) == k:
                    break
                res.append(num)

        return res