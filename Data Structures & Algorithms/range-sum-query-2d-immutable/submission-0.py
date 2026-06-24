class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, cols = len(matrix), len(matrix[0])
        self.matrix = [[0] * (cols + 1) for _ in range(row + 1)]
        
        for r in range(row):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.matrix[r][c + 1]
                self.matrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomright = self.matrix[r2][c2]
        above = self.matrix[r1 - 1][c2]
        left = self.matrix[r2][c1 - 1]
        topleft = self.matrix[r1 - 1][c1 - 1]

        return bottomright - above - left + topleft
