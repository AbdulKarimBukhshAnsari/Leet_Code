class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def count(n,nums):
            check = 0
            for i in nums:
                if i>=n:
                    check+=1
            return check

        for i in range(0,max(nums)+1):
            if i==count(i,nums):
                return i
        else:
            return -1
        
obj = Solution()
print(obj.specialArray())