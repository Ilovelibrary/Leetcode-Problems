class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        def explore(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]=='1':
                grid[i][j] = '0'
                explore(i-1,j)
                explore(i+1,j)
                explore(i,j-1)
                explore(i,j+1)
        
        m,n = len(grid),len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count += 1
                    explore(i,j)
        return count