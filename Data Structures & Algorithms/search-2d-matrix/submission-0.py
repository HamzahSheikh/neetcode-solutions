class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        p1 = 0
        p2 = m * n - 1

        while p1 <= p2:
            middle = p1 + (p2 - p1) // 2

            row = middle // n
            col = middle % n

            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                p1 = middle + 1
            else:
                p2 = middle - 1

        return False