
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        lst = []
        i = 0
        p_list = list(p)
        p_list.sort()
        while i <len(s)-len(p):
            if s[i] in p_list:
                temp = list(s[i:i+len(p)])
                temp.sort()
                if p_list ==temp:
                    lst.append(i)
            i+=1
        return lst
    
obj = Solution()
print(obj.findAnagrams("cbaebabacd","abc"))