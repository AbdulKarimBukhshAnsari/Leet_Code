class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target :
                        lst.append(i)
                        lst.append(j)
                        lst.sort()
                        return lst 

                
                  
obj = Solution()
print(obj.twoSum([3,2,3],6))