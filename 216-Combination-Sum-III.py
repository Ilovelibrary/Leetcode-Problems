class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        def combSum(path, i, k, n):
            if k==0 and n==0:
                self.res.append(path)
                return
            if k<=0 or n<=0:
                return
            for j in range(i,10):
                combSum(path+[j],j+1,k-1,n-j)            
        combSum([],1,k,n)
        return self.res