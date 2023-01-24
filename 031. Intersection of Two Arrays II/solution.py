class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
        
        dic = {}
        res = []
        for number in nums1:
            dic[number] = dic.get(number, 0) + 1
        
        for number in nums2:
            if number in dic and dic[number] > 0:
                res.append(number)
                dic[number] -= 1
        
        return res 