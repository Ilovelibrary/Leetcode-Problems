class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)<=3:
            return max(nums)
        l = len(nums)
        M1 = [0 for _ in range(l)]
        M2 = [0 for _ in range(l)]
        for i in range(l-1):
            M1[i] = max(nums[i]+M1[i-2],M1[i-1])
        for i in range(1,l):
            M2[i] = max(nums[i]+M2[i-2],M2[i-1])
        return max(M1[-2],M2[-1])
            