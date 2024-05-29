class Solution(object):
    def minimumSum(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        lst = []
        i = 1 
        while len(lst) != n:
            if all(i+lst[x]!=k for x in range(len(lst)) ):
                lst.append(i)
            i+=1
        return sum(lst)
obj = Solution()
print(obj.minimumSum(5,4))