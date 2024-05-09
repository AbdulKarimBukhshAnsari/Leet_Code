class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_of_list = set(nums)
        lst_of_set = list(set_of_list)
        lst_of_set.sort()
        nums = []
        nums.extend(lst_of_set)
        return len(nums)
nums = [1,1,1,2,3]
obj = Solution()
print(obj.removeDuplicates(nums))
print(nums)