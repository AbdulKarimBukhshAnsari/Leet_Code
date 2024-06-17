class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_list = [i for i in nums if nums.count(i)==1]
        return new_list[0]

obj = Solution()
