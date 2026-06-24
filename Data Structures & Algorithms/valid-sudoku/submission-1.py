class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set)
        rows=defaultdict(set)
        boxes=defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==".":
                    continue
                if (board[i][j] in rows[i] or board[i][j]in cols[j] or board[i][j] in boxes[(i//3,j//3)]):
                    return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                boxes[(i// 3, j // 3)].add(board[i][j])                
        return True