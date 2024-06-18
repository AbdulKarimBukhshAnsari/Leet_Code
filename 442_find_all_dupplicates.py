class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        nums.sort()
        lst = [nums[i] for i in range(len(nums)-1) if nums[i]==nums[i+1]]
        return lst