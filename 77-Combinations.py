class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        self.res = []
        def dfs(path, i, depth):
            if depth==0:
                self.res.append(path)
                return
            if depth<0:
                return
            for j in xrange(i,n+1):
                if n+1-j<depth-1:
                    break
                dfs(path + [j], j+1, depth-1)
        dfs([],1,k)
        return self.res
    
