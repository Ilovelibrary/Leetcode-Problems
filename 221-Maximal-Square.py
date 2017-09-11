class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        for i,s in enumerate(matrix):
            matrix[i]=[int(j) for j in s]
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==1:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]>res:
                    res = matrix[i][j]
        return res**2