class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict={}
        l=0
        ans=0

        for r in range(len(s)):
            if s[r] in dict:
                l=max(l,dict[s[r]]+1)
            dict[s[r]]=r
            ans=max(ans,r-l+1)
        
        return ans

            

                

