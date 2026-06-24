class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string=set()
        maxlen=0
        l=0
        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l+=1
            string.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen

