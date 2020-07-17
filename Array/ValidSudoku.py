# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
'''
The solution below is not the fastest because the code goes though the cells several times
but it was chosen for the better readability (i.e. checking the numbers in
rows / columns/ sub-boards is separate)
'''
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set possible_values will be used to check that the value in the cell is a valid one
        possible_values = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}

        length = len(board)
        for i in range(length):
            ''' arrays nums will be used to check that each number in validated section is unique
            'False' means that the number is not present in validated area
            '''
            nums_row = [False] * 9
            nums_column = [False] * 9
            nums_sub_board = [False] * 9
            # sub-board coordinates:
            x = i // 3
            y = i % 3
            for j in range(length):
                ''' i and j are used to run through cells:
                board[i][j] runs through rows
                board[j][i] runs through columns
                '''
                if board[i][j] not in possible_values:
                    return False
                # the code below checks that the number is unique in the ROW
                if board[i][j] != '.':
                    if nums_row[int(board[i][j]) - 1]:
                        return False
                    else:
                        nums_row[int(board[i][j]) - 1] = True
                # the code below checks that the number is unique in the COLUMN
                if board[j][i] != '.':
                    if nums_column[int(board[j][i]) - 1]:
                        return False
                    else:
                        nums_column[int(board[j][i]) - 1] = True
                # the code below checks that the number is unique in 3x3 SUB-BOARD
                # cell coordinates within 3x3 sub-board:
                x_local = j // 3
                y_local = j % 3
                if board[x * 3 + x_local][y * 3 + y_local] != '.':
                    if nums_sub_board[int(board[x * 3 + x_local][y * 3 + y_local]) - 1]:
                        return False
                    else:
                        nums_sub_board[int(board[x * 3 + x_local][y * 3 + y_local]) - 1] = True
        return True

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(board))
