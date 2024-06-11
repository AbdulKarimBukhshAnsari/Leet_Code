class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result1 = []
        for i in range(len(arr2)):  
            result1.extend([arr2[i]]*(arr1.count(arr2[i])))
        result2 = [i for i in arr1 if i not in arr2]
        result = result1+result2
        return result
        
obj = Solution()
print(obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))