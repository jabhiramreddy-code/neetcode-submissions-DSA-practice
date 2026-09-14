class Solution:
    def colCheck(self, board: List[List[str]]) -> bool:
        for i in range(9):
            contain = set()
            for j in range(9):
                element = board[i][j]
                if element in contain:
                    print(element)
                    return True
                if element != ".":
                    contain.add(element)
        return False
    
    def rowCheck(self, board: List[List[str]]) -> bool:
        for i in range(9):
            contain = set()
            for j in range(9):
                element = board[j][i]
                if element in contain:
                    print("asd")
                    print(element)
                    return True
                if element != ".":
                    contain.add(element)
        return False
    def minBox(self, rum: int, cum: int, board: List[List[str]]) -> bool:
        check = set()
        for i in range(3):
            for j in range(3):
                x = board[rum+i][cum+j]
                if x in check:
                    print(x)
                    return True
                if x != ".":
                    check.add(x)
        return False
    def boxCheck(self, board: List[List[str]]) -> bool:
        for i in range(0,9,3):
            for j in range(0,9,3):
                if self.minBox(i,j,board):
                    return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.colCheck(board):
            print(1)
            return False
        if self.rowCheck(board):
            print(2)
            return False
        if self.boxCheck(board):
            print(3)
            return False
        return True
        