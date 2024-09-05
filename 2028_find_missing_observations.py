class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        k = m+n
        sum_n = (k*mean)-sum(rolls)
        # Ensure that the value is less than the max possible value and greater than the min possible value so the max value could be n*6 and min value could be n .
        if (sum_n > n*6) or (sum_n<n):
            return [] 
        #using greedy algorithm 
        res = []
        while n:
            # the max possible value can be 6 so we first prioritize the 6 but there is one problem if we use then there is a chance that after choosing 6 we have n>sum_n so we simply use the condition that if the differce is less than 6 so we consider that value
            if  sum_n-n+1 > 6:
                result =6
            else:
                result = sum_n-n+1
            res.append(result)
            sum_n-=result
            n-=1
        return res



    


        