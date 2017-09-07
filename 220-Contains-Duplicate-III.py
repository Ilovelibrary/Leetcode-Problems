class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t<0:
            return False
        dic = {}
        w = t+1
        for i in range(len(nums)):
            bucket = nums[i]/w
            if bucket in dic:
                return True
            if bucket-1 in dic and abs(dic[bucket-1]-nums[i])<w:
                return True
            if bucket+1 in dic and abs(dic[bucket+1]-nums[i]<w):
                return True
            dic[bucket] = nums[i]
            if i>=k: 
                del dic[nums[i-k]/w]
        return False