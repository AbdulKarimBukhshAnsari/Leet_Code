class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        #using binary search
        start = min(bloomDay)
        end = max(bloomDay)
        mid = (start+end)//2
        while start<=end :
            flower = 0
            bouqet = 0 
            for day in bloomDay:
                if day <= mid:   # checking whether this number is greater than mid or not if t is greater than mid it means that our flower has bloomed 
                    flower+=1
                    if flower == k: #check if the flower is euqual to k then it means our bouqet has been made
                        flower = 0 #then we will make it zero it means that flower has been used 
                        bouqet+= 1 #one bouqet has been made
                        if bouqet==m:
                            break
                else:
                    flower = 0  # but if the day is less than mid then flower will be zero because we need adjacent flower  
            if bouqet >= m:
                result =  mid
                end = mid -1
    
            else:
                start= mid+1
            mid = (start+end)//2
        return result
obj = Solution()
print(obj.minDays([1,10,3,10,2],3,1))

            
        
