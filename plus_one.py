class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = ""
        for i in digits:
            digit+=str(i)
        number = str(int(digit)+1)
        lst = [int(i) for i in number]
        return lst

obj = Solution()
print(obj.plusOne([1,2,3]))
