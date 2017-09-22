class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        dAB = collections.Counter()
        for a in A:
            for b in B:
                dAB[a+b] += 1
        dCD = collections.Counter()
        res = 0
        for c in C:
            for d in D:
                res += dAB[-c-d]
        return res
