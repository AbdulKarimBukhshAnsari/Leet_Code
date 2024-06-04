class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = dict()
        result = 0
        #counting the each character that how much time it has appeared
        for i in s:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i] = 1
        check_odd = False
        for j in hash_map.values():
            if j%2==0:  #checkin the count of each charcter 
                result+=j
            else:
                result+=j-1   #if the count of eac charcter is one then the count of result will be increased by just 0 but if there is any odd number like 3,5 then it will decrese aby 1 unit            
                check_odd=True  
        if check_odd == True:
            result+=1
        return result
obj = Solution()
print(obj.longestPalindrome("abccccdd"))