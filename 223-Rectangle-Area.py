class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        S1 = abs(C-A)*abs(D-B)
        S2 = abs(G-E)*abs(H-F)
        a = g = max(A,E)
        d = b = max(B,F)
        c = e = min(C,G)
        f = h = min(D,H)
        if c-a<=0 or f-d<=0:
            return S1+S2
        else:
            return S1+S2-abs(c-a)*abs(f-d)