class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        crew=defaultdict(int)
        judge=defaultdict(int)
        for x,y in trust:
            crew[x]+=1
            judge[y]+=1

        for key,value in judge.items():
            if value==n-1 and key not in crew:
                return key

        return -1