class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        
        countt={}
        counts={}
        for ch in t:
            countt[ch]=countt.get(ch,0)+1
        need=len(countt)
        have=0
        res,reslen=[-1,-1],float("inf")
        l=0
        for r in range(len(s)):
            ch=s[r]
            counts[ch]=counts.get(ch,0)+1

            if ch in countt and counts[ch]==countt[ch]:
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
                            
            

