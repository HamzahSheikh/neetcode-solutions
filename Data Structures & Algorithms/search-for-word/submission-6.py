class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        y = len(board)
        x = len(board[0])


        def backtracking(row, col, index, seen) -> bool:
            
            if index == len(word):
                return True

            if row == y or col == x or row == -1 or col == -1:
                return False

            curr = board[row][col]
            coordinates = (row, col)

            if curr != word[index] or coordinates in seen:
                return False

            index += 1
            seen.add(coordinates)

            ans = backtracking(row+1, col, index, seen) or backtracking(row, col+1, index, seen) or backtracking(row-1, col, index, seen) or backtracking(row, col-1, index, seen)
            seen.remove(coordinates)
            return ans

        for row in range(0, y):
            for col in range(0, x):
                curr = board[row][col]
                coordinates = (row, col)

                if curr == word[0]:
                    if backtracking(row, col, 0, set()):
                        return True

        return False
        

        