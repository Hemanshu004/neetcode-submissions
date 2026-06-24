class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        
        counts={}
        countt={}
        for ch in t:
            countt[ch]=countt.get(ch,0)+1
        have,need=0,len(countt)
        res,reslen=[-1,-1],float("inf")
        l=0
        for r in range(len(s)):
            c=s[r]
            counts[c]=counts.get(c,0)+1
            
            if c in countt and counts[c]==countt[c]:
                have+=1

            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                counts[s[l]]-=1
                if s[l] in countt and countt[s[l]]>counts[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("inf") else ""
