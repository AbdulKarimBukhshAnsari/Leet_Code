class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in range(len(pref)):
            if i==0:
                lst.append(pref[0]) #first element would be same 
            else:
                result_xor = lst[i-1] ^ lst[i]
                lst.append(result_xor) 