class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        check = {1:"qwertyuiop",2:"asdfghjkl",3:"zxcvbnm"}
        result = []
        for i in words:
            if all(x in check[1] for x in i.lower() ) == True or all(x in check[2] for x in i.lower() ) == True or all(x in check[3] for x in i.lower() ) == True:
                result.append(i)
        return result
obj = Solution()
print(obj.findWords(["Hello","Alaska","Dad","Peace"]))

