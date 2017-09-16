class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        pos = 1
        time, temp = 0, n
        while temp>1:
            temp /= 2
            time += 1
        #print time
        head,end = 1,n
        left,right = True, False
        length = n
        for i in range(time):
            if head==end:
                return head
            if n%2==1:
                head += 2**i
                end -= 2**i
            elif left and n%2==0:
                head += 2**i
            elif right and n%2==0:
                end -= 2**i
            n /= 2
            left,right = right,left
            #print head,end
        return head