class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        visit=set()

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]=="X" or (r,c) in visit:
                return
            
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            


        for r in range(rows):
            if board[r][cols-1]=="O":
                dfs(r,cols-1)
            if board[r][0]=="O":
                dfs(r,0)
        
        for c in range(cols):
            if board[rows-1][c]=="O" :
                dfs(rows-1,c)
            if board[0][c]=="O":
                dfs(0,c)
        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and board[r][c]=="O":
                    board[r][c]="X"
        
            



