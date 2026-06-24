class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict={}
        l=0
        res=0
        for i in range(len(s)):
            if s[i] in dict:
                l=max(dict[s[i]]+1,l)
            dict[s[i]]=i
            res=max(res,i-l+1)
        return res
            
