    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def compute(d1,d2,d3,d4):
            return (d1*10+d2)*60+(d3*10+d4)
        def decomp(num):
            m1,num = num%10,num/10
            m2,num = num%6,num/6
            h1,num = num%10,num/10
            h2,num = num%6,num/6
            return h2,h1,m2,m1
        d1,d2,d3,d4 = int(time[0]),int(time[1]),int(time[-2]),int(time[-1])
        All = [d1,d2,d3,d4]
        Time = compute(d1,d2,d3,d4)
        for i in xrange(Time+1,24*60):
            h2,h1,m2,m1 = decomp(i)
            if h1 in All and h2 in All and m2 in All and m1 in All:
                return str(h2)+str(h1)+':'+str(m2)+str(m1)
        m = min(All)
        return str(m)+str(m)+':'+str(m)+str(m)
