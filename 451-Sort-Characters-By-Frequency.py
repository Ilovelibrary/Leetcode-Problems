class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        l = []
        for key, value in dic.iteritems():
            l.append((value,key))
        l = sorted(l,reverse=True)
        res =''
        for pair in l:
            res += pair[1]*pair[0]
        return res