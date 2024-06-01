class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1))



obj = Solution()
print(obj.scoreOfString("hello"))
        