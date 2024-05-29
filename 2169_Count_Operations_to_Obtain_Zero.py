class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        result = 0
        while (num1!=0) and (num2!=0):
            if num1>=num2:
                num1-=num2
            else:
                num2-=num1
            result+=1
        return result
obj = Solution()
print(obj.countOperations(2,3))

            