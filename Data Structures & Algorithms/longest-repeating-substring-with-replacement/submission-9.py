class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict()
        maxf=0
        l=0
        maxlen=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            maxf=max(maxf,count[s[r]])
        
            if (r-l+1)-maxf >k:
                count[s[l]]-=1
                l+=1
        
            maxlen=max(maxlen,r-l+1)
        
        return maxlen
        



