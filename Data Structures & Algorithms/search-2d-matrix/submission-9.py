class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        rows=row-1
        for r in range(row-1):
            if matrix[r][0]<=target<matrix[r+1][0]:
                rows=r
                break
        
        for c in range(col):
            if matrix[rows][c]==target:
                return True
        return False
