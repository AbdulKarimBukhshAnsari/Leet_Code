class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        check = False
        if x<0:
            x_str = str(x)
            x = int(x_str[1:])
            check = True
        reverse_num = ""
        while x>0:
            reverse_num += str(x%10)
            x = int(x/10)
        if reverse_num<-2**31 or reverse_num>2**31 -1:
            return 0
        if check == True:
            return int("-"+reverse_num)
        else:
            return int(reverse_num)


obj = Solution()
print(obj.reverse(4567))

