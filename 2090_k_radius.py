class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k > len(nums):
            return [-1 for _ in range(nums)]
        lst = []
        for i in range(k,len(nums)-k):
            lst.append(int(sum(nums[i-k:i+k+1])/len(nums[i-k:i+k+1])))
        return [-1 for _ in range(k)] + lst + [-1 for _ in range(k)]
obj = Solution()
print(obj.getAverages([100000],0))
        



        
