class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums)<3:
            return nums.index(max(nums))
        for i in range(0,len(nums)):
            if i ==0:
                if nums[i]>nums[i+1]:
                    return i
            elif i==len(nums)-1:
                if nums[i]>nums[i-1]:
                    return i
            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i 