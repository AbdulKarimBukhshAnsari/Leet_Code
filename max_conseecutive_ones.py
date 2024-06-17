class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_check = 0
        check = 0
        for i in range(len(nums)):
            if nums[i]== 1:
                check+=1
            else:
                if check > max_check:
                    max_check = check
                    check = 0
        if check>max_check:
            max_check = check 
        return max_check
obj = Solution()
print(obj.findMaxConsecutiveOnes())