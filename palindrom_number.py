class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_number = str(x)
        if string_number == string_number[::-1]:
            return True
        else:
            return False

obj = Solution()
print(obj.isPalindrome(-121))
        