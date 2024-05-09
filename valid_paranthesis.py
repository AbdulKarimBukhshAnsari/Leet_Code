class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = False
        for i in range(len(s)):
            if i%2 == 0:
                if s[i] == "{" and s[i+1] == "}":
                    result = True
                elif s[i] == "(" and s[i+1] == ")":
                    result = True
                elif s[i] == "[" and s[i+1] == "]":
                    result = True
                else:
                    result = False
        return result
                    
                


obj = Solution()
print(obj.isValid("()"))          
                    