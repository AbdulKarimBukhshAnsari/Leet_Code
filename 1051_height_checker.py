class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sortt = heights[:]
        sortt.sort()
        check = 0
        for i in range(len(sortt)):
            if sortt[i]!= heights[i]:
                check+=1
        return check 