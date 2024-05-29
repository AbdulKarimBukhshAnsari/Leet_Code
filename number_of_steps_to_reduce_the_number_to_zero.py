class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        while num!=0:
            if num%2==0:
                num=num/2
            else:
                num-=1
            result+=1
        return result