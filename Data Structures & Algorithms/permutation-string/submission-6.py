class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        countl=[0]*26
        countr=[0]*26

        for i in range(len(s1)):
            countl[ord(s1[i])-ord('a')]+=1
            countr[ord(s2[i])-ord('a')]+=1
        
        if countl==countr:
            return True
        
        l=0
        for r in range(len(s1),len(s2)):
            countr[ord(s2[r])-ord("a")]+=1
            countr[ord(s2[l])-ord("a")]-=1
            l+=1
            if countr==countl:
                return True
        return False