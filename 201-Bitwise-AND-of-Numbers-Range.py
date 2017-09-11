class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = m&n
        d = m-n
        res >>= len(bin(d))-3
        res <<= len(bin(d))-3
        return res
        