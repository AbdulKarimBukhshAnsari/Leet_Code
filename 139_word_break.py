class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for i in wordDict:
            string = s
            if i in s:
                string = s[s.index(i[0]):s.index(i[-1])]
            else:
                return False
        else:
            return True
        #not solved