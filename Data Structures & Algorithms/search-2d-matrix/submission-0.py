class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        top,bot = 0 , m-1
        while top <=bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row +1
            elif target < matrix[row][0]:
                bot = row - 1;
            else:
                break;
        if not top <= bot:
            return False;
        i,j=0,n-1
        row = (top+bot)//2
        while i<=j:
            mid = (i+j)//2
            if target < matrix[row][mid]:
                j = mid-1
            elif target > matrix[row][mid]:
                i = mid + 1
            else:
                return True
        return False


        