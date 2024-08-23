class Solution:
    def findComplement(self, num: int) -> str:
        str_comp = ""
        while num>=1:
            str_comp +=str(num%2)
            num = num//2
        str_comp = str_comp[::-1]
        result = 0
        for i in range(len(str_comp)):
            if int(str_comp[len(str_comp)-i-1]) == 0:
                result+=2**i
        return result
       
obj = Solution()
print(obj.findComplement(5))

