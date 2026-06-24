class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount={}
        tcount={}
        for i in s:
            scount[i]=scount.get(i,0)+1
        for j in t:
            tcount[j]=tcount.get(j,0)+1
        if scount==tcount:
            return True
        return False