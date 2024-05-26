class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 1
        while i<=int(len(s)/2):
            now = s[:i]
            if len(s)%len(now) == 0:
                if s.count(now) == len(s)/len(now):
                    return True
            i+=1
        
        return False
obj = Solution()
print(obj.repeatedSubstringPattern("abab"))