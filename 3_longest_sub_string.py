class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        start = 0
        end = 1
        max_len = 0
        while end<= len(s):
            if all(s[start:end].count(x)<2  for x in s[start:end]) == True:
                end+=1
                
            else:
                max_len = max(max_len,len(s[start:end-1]))
                start+=1
        max_len = max(max_len,len(s[start:end-1]))

        return max_len
            

#yeepee solved after 2 month xd