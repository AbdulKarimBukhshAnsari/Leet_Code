class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = []
        for i in nums:
            if i not in nums1:
                nums1.append(i)
        print(nums1)
        if len(nums1)<3:
            return max(nums1)
        nums1.remove(max(nums1))
        nums1.remove(max(nums1))
        return max(nums1)
    
obj = Solution()
print(obj.thirdMax([2,2,3,1]))