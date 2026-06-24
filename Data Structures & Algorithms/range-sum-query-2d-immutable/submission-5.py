class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        Rows,Cols=len(matrix),len(matrix[0])
        self.summat=[[0]*(Cols+1)for _ in range(Rows+1)]
        for r in range(len(matrix)):
            prefix=0
            for c in range(len(matrix[0])):
                prefix+=matrix[r][c]
                above=self.summat[r][c+1]
                self.summat[r+1][c+1]=prefix+above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2=row1+1,row2+1,col1+1,col2+1
        left=self.summat[r2][c1-1]
        right=self.summat[r1-1][c2]
        topleft=self.summat[r1-1][c1-1]
        bottom=self.summat[r2][c2]
        return bottom-left-right+topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)