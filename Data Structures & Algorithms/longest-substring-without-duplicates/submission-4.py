class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        re=set()
        maxlen=0
        l=0
        for r in range(len(s)):
            while s[r] in re:
                re.remove(s[l])
                l+=1
            re.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen
