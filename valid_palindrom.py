class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower_s = s.lower()
        s_without_space = ''.join(i for i in lower_s if i.isalpha() or i.isdigit())
        if s_without_space == s_without_space[::-1]:
            return True
        else:
            return False
obj = Solution()
print(obj.isPalindrome("0P"))