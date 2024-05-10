class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        lst = [0 for i in range(len(score))]
        lst2 = score[:]
        for i in range(len(score)):
            max_element = max(lst2)
            index_element = score.index(max_element)
            if i == 0:
                lst[index_element] = "Gold Medal"
            elif i == 1:
                lst[index_element] = "Silver Medal"
            elif i == 2:
                lst[index_element] = "Bronze Medal"
            else:
                lst[index_element] = str(i+1)
            lst2.remove(max_element)
        return lst

obj = Solution()
print(obj.findRelativeRanks([5,4,3,2,1]))
#not completed
            

        