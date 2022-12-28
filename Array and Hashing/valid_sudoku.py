# -*- coding: utf-8 -*-
"""Valid Sudoku.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u1Kp1DVw5L8QeYa1pAKqKudcoVg60Ro9
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        boxes=collections.defaultdict(set)
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]=='.':
                    continue
                if(
                    board[i][j]in rows[i]
                    or board[i][j]in cols[j]
                    or board[i][j] in boxes[(i//3,j//3)]
                ) :

                   return False  
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                
                boxes[(i//3,j//3)].add(board[i][j]) 
        return True