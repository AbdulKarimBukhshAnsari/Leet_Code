class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        arr1_prefix_set = set()
        for i in arr1:
            while i > 0 :
                arr1_prefix_set.add(i)
                i = i//10
        arr2_prefix_set = set()
        for i in arr2:
            while i > 0 :
                arr2_prefix_set.add(i)
                i = i//10
        intersect = arr1_prefix_set & arr2_prefix_set
        if not intersect:
            return 0
        return len(str(max(intersect)))


