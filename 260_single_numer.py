class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = [x for x in nums if nums.count(x)==1]
        return lst 