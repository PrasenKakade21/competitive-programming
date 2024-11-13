from typing import List 
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_map = defaultdict(set)
        
        for col in range(0,9):
            col_map = defaultdict(int)
            row_map = defaultdict(int)
            for row in range(0,9):
                x = board[col][row]
                if x != ".":
                    row_map[x] += 1
                    if row_map[x] > 1:
                        return False
                    if x in box_map[((row // 3, col // 3))]:
                        return False
                    box_map[(row // 3, col // 3)].add(x)
                y = board[row][col]
                if y != ".":
                    col_map[y] += 1 
                    if col_map[y] > 1:
                        return False
            print("box " ,box_map)
            print(row_map) 
            print(col_map) 
            
        return True
                
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

s = Solution
print(s.isValidSudoku(s,board))