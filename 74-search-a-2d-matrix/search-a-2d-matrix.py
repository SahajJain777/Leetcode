class Solution(object):
    def searchMatrix(self, matrix, target):
        last = len(matrix[0])-1
        m = 0
        for i in range(len(matrix)):
            if(target<=matrix[i][last]):
                m = i
                break
            
        for j in range(last+1):
            if(target == matrix[m][j]):
                return True

        return False
        

        