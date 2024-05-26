class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """I will apply here the operation of difference
        in set which will subtract the set and will tell us which elements
        does not present in another set and after that we made the list of this set""" 
        return list(set(range(1,len(nums)+1))-set(nums))
        
obj = Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))