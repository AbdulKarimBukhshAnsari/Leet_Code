class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value = min(prices)
        start = prices.index(min_value)
        if start+1==len(prices):
            return 0  
        max_revenue = prices[start+1:]
        if min_value>= max(max_revenue):
            return 0
        else:
            return max(max_revenue) - min_value
obj = Solution()
print(obj.maxProfit([7,6,4,3,1]))

        
        

