class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        result = []
        potions.sort()
        for i in spells:
            start ,end , temp_result = 0,len(potions)-1,len(potions)
            #we took the temp_result == 0 so that if there is no success value then we can easily append the 0
            while start<=end:
                mid = (start+end)//2
                if i*potions[mid]>=success:
                    end = mid-1
                    temp_result = mid
                    #save the least true result so if there is no true result then we can return least 
                else:
                    start=mid+1
            result.append(len(potions)-temp_result) # It will let us know the right side element which all the satisfied
        return result