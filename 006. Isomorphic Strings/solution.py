# solution1:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s_t = {}
        dic_t_s = {}
        for i in range(len(s)):
            if s[i] not in dic_s_t.keys() and t[i] not in dic_t_s.keys():
                dic_s_t.update({s[i]:t[i]})
                dic_t_s.update({t[i]:s[i]})
            elif dic_s_t.get(s[i]) != t[i] or dic_t_s.get(t[i]) != s[i]:
                return False

        return True


# solution2:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))