class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = len(strs[0])
        for i in range(1,len(strs)):
            while result!=0:
                if result>len(strs[i]):
                    result = len(strs[i])
                if strs[0][:result] != strs[i][:result]:
                    result-=1
                else:
                    break
        return strs[0][:result]
                
        
obj = Solution()
print(obj.longestCommonPrefix(["dog","racecar","car"]))       
        
        
