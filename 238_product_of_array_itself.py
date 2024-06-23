class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_mult = [1]*len(nums)
        prod1 = 1
        for i in range(len(nums)):
            prod1 = prod1*nums[i]
            prefix_mult[i] = prod1
        postfix_mult = [1]*len(nums)
        prod1 = 1
        for i in range(len(nums)-1,-1,-1):
            prod1 = prod1*nums[i]
            postfix_mult[i] = prod1
        i = -1
        j = 1
        lst = [1]*len(nums)
        count = 0
        while i<=len(nums)-2:
            if i == -1 :
                lst[count] = 1*postfix_mult[j]
            elif i == len(nums) -2 :
                lst[count] = prefix_mult[i]*1
            else:
                lst[count] = prefix_mult[i] * postfix_mult[j]
            i+=1
            j+=1
            count+=1
        return lst 



obj = Solution()
print(obj.productExceptSelf([1,2,3,4]))  
        

