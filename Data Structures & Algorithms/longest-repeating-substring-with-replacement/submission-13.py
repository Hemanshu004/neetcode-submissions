class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        maxf=0
        maxLength=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            if count[s[r]]>maxf:
                maxf=count[s[r]]
            
            if (r-l+1)-maxf >k:
                count[s[l]]-=1
                l+=1
            
            maxLength=max(maxLength,r-l+1)

        return maxLength

