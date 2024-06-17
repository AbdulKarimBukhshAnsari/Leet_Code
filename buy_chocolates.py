class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        check = 0  # checkinh how much chocolate he has bought
        result = money #making copy of the money to work on that without adjusting the actual value
        for i in range(2): # to run the loop for 2 times
            if any(x<=money for x in prices): #check whether you are able to buy the choclate or not .
                result-=min(prices) #deduct the value
                if result<0:   #if result will become less than zero it means you are not able to buy this
                    return money #return the actual money because you are not able to buy 
                prices.remove(min(prices))
                check+=1

        if check>1: # check whether you have bought the chocolate times or not
            return result 
        else:
            return money 


        