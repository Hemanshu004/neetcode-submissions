class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT={}
        for i in t:
            countT[i]=countT.get(i,0)+1
        res,reslen=[-1,-1],float("inf")
        for i in range(len(s)):
            countS={}
            for j in range(i,len(s)):
                countS[s[j]]=1+countS.get(s[j],0)

                flag=True
                for c in countT:
                    if countT[c]>countS.get(c,0):
                        flag=False
                        break 
                    
                if flag and (j-i+1)<reslen:
                    reslen=j-i+1
                    res=[i,j]

        l,r=res
        return s[l:r+1] if reslen!=float("inf") else ""