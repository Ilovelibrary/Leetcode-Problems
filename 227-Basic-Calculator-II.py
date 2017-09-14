class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        for i in xrange(len(s)-1,-1,-1):
            if s[i] in ['+','-','*','/']:
                nums = [int(s[i+1:])] + nums
                nums = [str(s[i])] + nums
                s = s[:i]
        nums = [int(s[i])] + nums
        print nums
        stack = []
        while nums:
            item = nums.pop(0)
            if item=='*' and stack:
                num2 = nums.pop(0)
                num1 = stack.pop()
                stack.append(num1*num2)
            elif item=='/' and stack:
                num2 = nums.pop(0)
                num1 = stack.pop()
                stack.append(num1/num2)
            else:
                stack.append(item)
        print stack
        res = 0
        while stack:
            item = stack.pop(0)
            if item=='+':
                num = stack.pop(0)
                res += num
            elif item=='-':
                num = stack.pop(0)
                res -= num
            else:
                res += item
        return res
        