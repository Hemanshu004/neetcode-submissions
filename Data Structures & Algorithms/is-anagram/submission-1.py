from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}

        for i in s:
            dict_s[i]=1 + dict_s.get(i,0)
        for i in t:
            dict_t[i]=1+dict_t.get(i,0)

        if len(s)==len(t) and dict_s==dict_t:
            return True
        else:
            return False
