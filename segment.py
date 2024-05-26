class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = s.split()
        return len(p)
obj = Solution()
print(obj.countSegments("Hello, my name is John"))