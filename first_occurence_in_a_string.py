class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        j = 0
        if needle in haystack:   
            for i in range(len(haystack)):
                if i % len(needle) == 0:
                    if needle == haystack[i:i+len(needle)]:

                        return j
                j+=1
        else:
            j =-1
            return j 
                
            

obj = Solution()
print(obj.strStr("hello","ll"))
#not solved