class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        check = False
        dict1 = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        dict2 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            if check == True:
               check =False
            elif s[i:i+2] in dict1:
               check = True
               integer+=dict1[s[i:i+2]]
            elif s[i] in dict2:
                integer+=dict1[s[i]]
        return integer
        

obj = Solution()
            

                  