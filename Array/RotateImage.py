# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ''' The idea is that when matrix is rotating 4 cells are moving to each other place
        at the same time (after four rotations by 90 degree these cells return to their
        original positions)

        exception - central cell when matrix has odd length of the side
        below _iterations_ is the number of these FOURs that we will move within one iteration
        '''
        length = len(matrix)
        iterations = length ** 2 // 4
        row = 0
        col = 0
        for iteration in range(iterations):
            '''the coordinates of the cells that are moving to each other place are:
            [row,col] <- [col,length-1-row] <- [length-1-row, length-1-col] <- 
            <- [length-1-col, row] <- [row,col] (original position)
            the code below will 'rotate' the triangle within the matrix that lays between
            matrix center - left upper corner of the matrix - left lower corner of the matrix
            this triangle represents all [row,col] cells '''
            k = length - 1 - row
            n = length - 1 - col
            m = matrix
            m[col][k], m[k][n], m[n][row], m[row][col] = m[row][col], m[col][k], m[k][n], m[n][row]

            row += 1
            if row == (length - 1 - col):
                col += 1
                row = col

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
'''matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]'''
Solution().rotate(matrix)
print("Final matrix: ")
for p in range(len(matrix)):
    print(matrix[p])
