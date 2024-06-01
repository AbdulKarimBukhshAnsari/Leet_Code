class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = s.split()[::-1]
        return  ' '.join(p)
obj = Solution()
print(obj.reverseWords("  hello world  "))
