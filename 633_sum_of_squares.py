class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #using two pointers for this concept 
        start = 0
        end = int(c **(1/2))   #end point should be the root of this number 
        while start<=end:
            print(start,end)
            if c == start*start+end*end:
                return True
            elif c<start*start +end*end:
                end-=1
            elif c>start*start + end*end:
                start+=1
        return False
obj = Solution()
print(obj.judgeSquareSum(5))