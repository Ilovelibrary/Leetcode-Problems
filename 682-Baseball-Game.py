class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        def func(x):
            try:
                x=int(x)
                return isinstance(x,int)
            except ValueError:
                return False
        stack = []
        for i in xrange(len(ops)):
            op = ops[i]
            if func(op):
                stack.append(int(op))
            elif op=='D':
                stack.append(stack[-1]*2)
            elif op=='+':
                stack.append(stack[-1]+stack[-2])
            elif op=='C':
                stack.pop()
        return sum(stack)
