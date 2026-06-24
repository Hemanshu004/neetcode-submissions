class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat=set()
        l=0
        maxlen=0
        for r in range(len(s)):
            while s[r] in repeat:
                repeat.remove(s[l])
                l+=1
            repeat.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen