class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag = True
        for i in range(len(s)):
            if s[i] in t:
                if i == len(s) -1 :
                    if t.index(s[i])>t.index(s[i-1]):
                        pass
                    else:
                        return flag
                else:    
                    if t.index(s[i]) < t.index(s[i+1]):
                        pass
                    else:
                        flag = False
                        return flag  
            else:
                flag = False
                return flag
        return flag
            
       
