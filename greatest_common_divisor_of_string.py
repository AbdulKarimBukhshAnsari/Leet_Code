class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) <= len(str2):
            temp = str2
            str1 = str2
            str2 = temp
        stringg = ""
        j = len(str2)
        while j!=0:
            check = 0
            if str2[:j] == str1[:j]:
                check+=1
                if str2[:j] == str1[j:2*j]:
                    check+=1
        
            if check>1:
                stringg =str2[:j]
                return stringg
            j-=1
            if j==0:
                return stringg 
            check = 0       
obj = Solution()
print(obj.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))





        
    
