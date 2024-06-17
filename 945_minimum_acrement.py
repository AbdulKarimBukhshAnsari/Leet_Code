class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        lst = []
        for i in nums:
            if nums.count(i)>1 and i not in lst:
                lst.append(i)
        j=1
        result = 0
        for i in lst:
            while True:
                if j not in nums:
                    result+=j-i
                    j+=1
                    break
                j+=1
               
        return result
#not solved
            
                    

                    
        


obj = Solution()
print(obj.minIncrementForUnique([3,2,1,2,1,7]))
        