class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        while s[-1]==' ':
            s = s[:-1]
        ops = set(['+','-','*','/'])
        nums = []
        i,j = 0,0
        num = ''
        for i in xrange(len(s)):
            if s[i] in ops:
                nums.append(num)
                nums.append(s[i])
                num = ''
            elif s[i].isdigit():
                num = num+s[i]
                if i==len(s)-1:
                    nums.append(num)
        s = nums
        #print s
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                stack.append(int(s[i]))
                i += 1
                continue
            if s[i]=='+' or s[i]=='-':
                stack.append(s[i])
                i += 1
                continue
            if s[i]=="*":
                stack[-1] = stack[-1]*int(s[i+1])
                i += 2
            elif s[i]=="/":
                stack[-1] = stack[-1]/int(s[i+1])
                i += 2
        #print stack
        i = 0
        res = 0
        stack = ['+'] + stack
        while i < len(stack):
            if stack[i]=="+":
                res = res + stack[i+1]
                i += 2
            elif stack[i]=="-":
                res = res - stack[i+1]
                i += 2
        return res
