class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if len(set([tuple(p1),tuple(p2),tuple(p3),tuple(p4)]))!=4:
            return False
        l12 = (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        l13 = (p1[0]-p3[0])**2+(p1[1]-p3[1])**2
        l14 = (p1[0]-p4[0])**2+(p1[1]-p4[1])**2
        l23 = (p2[0]-p3[0])**2+(p2[1]-p3[1])**2
        l24 = (p2[0]-p4[0])**2+(p2[1]-p4[1])**2
        l34 = (p4[0]-p3[0])**2+(p4[1]-p3[1])**2
        lis = sorted([l12,l13,l14,l23,l24,l34])
        if lis[0]==lis[1]==lis[2]==lis[3] and lis[4]==lis[5]:
            return True
        else:
            return False
