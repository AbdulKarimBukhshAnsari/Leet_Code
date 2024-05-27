class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        poison_time = 0
        for i in range(len(timeSeries)):
            if i==len(timeSeries)-1:
                poison_time+=duration
                return poison_time
            if timeSeries[i+1] > timeSeries[i]+duration:
                poison_time+=duration
            else:
                print(False)
                poison_time+=timeSeries[i+1] - timeSeries[i]
        return poison_time    
            
obj = Solution()
print(obj.findPoisonedDuration([1,3,5,7,9,11,13,15],3))