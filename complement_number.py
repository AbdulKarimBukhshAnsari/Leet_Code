class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary_num = bin(num)[2:]
        prefix = bin(num)[:2] 
        complement_string = prefix+''.join(("0" if i=="1" else "1" for i in binary_num))
        return int(complement_string,base=2)

obj = Solution()
print(obj.findComplement(5))