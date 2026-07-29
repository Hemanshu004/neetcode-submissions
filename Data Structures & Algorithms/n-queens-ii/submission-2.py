class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        negd=set()
        posd=set()

        board=[["."]*n for i in range(n)]
        self.res=0

        def dfs(r):
            if r==n:
                self.res+=1
                return 
            
            for c in range(n):
                if c in cols or (r+c) in posd or (r-c) in negd:
                    continue
                
                cols.add(c)
                posd.add(r+c)
                negd.add(r-c)
                dfs(r+1)
                cols.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
            
        dfs(0)
        return self.res
            
