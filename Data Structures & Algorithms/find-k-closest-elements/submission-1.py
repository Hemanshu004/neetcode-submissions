class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        while k>0:
            diff=float("inf")
            closest=None
            for a in arr:
                d=abs(x-a)
                if d<diff:
                    diff=d
                    closest=a
                elif d==diff:
                    closest=min(closest,a)
            res.append(closest)
            arr.remove(closest)
            k-=1
        return sorted(res)
