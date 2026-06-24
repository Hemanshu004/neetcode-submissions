class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row=len(board)
        cols=len(board[0])
        q=deque()
        for i in range(row):
            for j in range(cols):
                if board[i][j] == "O" and (i == 0 or i == row-1 or j == 0 or j == cols-1):
                    board[i][j] = "T"
                    q.append((i,j))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            i,j = q.popleft()
            for dr, dc in directions:
                r, c = i + dr, j + dc
                if 0 <= r < row and 0 <= c < cols and board[r][c] == "O":
                    board[r][c] = "T"
                    q.append((r,c))

        for i in range(row):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"