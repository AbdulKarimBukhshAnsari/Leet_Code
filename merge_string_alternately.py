class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge_string = ""
        if len(word1)>len(word2):
            for i in range(len(word1)):
                merge_string+=word1[i]
                if i <= (len(word2)-1):
                    merge_string +=word2[i]
            return merge_string
        else:
            for i in range(len(word2)):
                if i <= (len(word1)-1):
                    merge_string +=word1[i]
                merge_string+=word2[i]
            return merge_string


obj = Solution()
word1 = input("Enter the 1st string: ")
word2 = input("Enter the second string: ")
print(obj.mergeAlternately(word1,word2))