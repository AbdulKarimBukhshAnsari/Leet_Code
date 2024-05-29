class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = int(s,2)
        result = 0
        while number!=1:
            if number%2==0:
                number = number/2
            else:
                number+=1
            result+=1
        return result
                

obj = Solution()
print(obj.numSteps("1101"))
