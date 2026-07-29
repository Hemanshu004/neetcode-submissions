class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        posD=set()
        negD=set()

        board=[["."]*n for i in range(n)]
        self.res=0

        def backtrack(r):
            if r==n:
                self.res+=1
                return 

            for c in range(n):
                if c in cols or(r+c) in posD or (r-c) in negD:
                    continue
                    
                cols.add(c)
                posD.add(r+c)
                negD.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                cols.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return self.res