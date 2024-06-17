class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        current_string = ""
        for i in s:
            if i not in current_string:
                current_string+=i
            else:
                if len(current_string)>max_len:
                    max_len = len(current_string)
                current_string = ""
                current_string+=i
        if len(current_string)>max_len:
            return len(current_string)
        return max_len
obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))
