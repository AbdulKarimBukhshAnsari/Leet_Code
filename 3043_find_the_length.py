class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        long = 0
        if len(arr1) > len(arr2):
            temp = arr2
            arr2 = arr1
            arr1 = temp
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                common_prefix = ''.join(c[0] for c in zip(word1,word2) if c[0] == [1])
word1 = "flower"
word2 = "flow"
common_prefix = len(''.join(c[0] for c in zip(word1, word2) if c[0] == c[1]))
print(common_prefix)
