class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while(i<=n):
            n = n-i
            i+=1
        return i-1 # since the increment is performed and the condition of while loop is not true so that we will subtract one value 
    
obj = Solution()
print(obj.arrangeCoins(5))