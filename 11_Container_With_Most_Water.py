class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        start = 0
        end = len(height)-1
        while start<=end:
            if height[start]<=height[end]:
                if height[start]*(end-start) >=max_area:
                    max_area = height[start]*(end-start)
                start+=1
            else:
                if height[end]*(end-start)>=max_area:
                    max_area = height[end]*(end-start)
                end-=1
        return max_area
obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
nums = [4,3,45,56]
print(nums[0:1])
