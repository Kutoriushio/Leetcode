class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for st in strs:
            counts = [0]*26
            for i in st:
                counts[ord(i) - ord('a')] += 1

            dic[tuple(counts)].append(st)
        
        return list(dic.values())