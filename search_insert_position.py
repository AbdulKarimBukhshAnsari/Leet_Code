class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        else:
            return nums.index(target)
obj = Solution()
print(obj.searchInsert([1,3,5,6],2))
        