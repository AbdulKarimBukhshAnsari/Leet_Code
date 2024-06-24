class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        from collections import Counter
        from math import factorial
        count = 0
        lst = [rectangles[x][0]/rectangles[x][1] for x in range(len(rectangles))]
        print(lst)
        hash_map = Counter(lst)
        print(hash_map)
        for i in hash_map:
            if hash_map[i] != 1:
                count += factorial(hash_map[i]-1)
        return count 

obj = Solution()
print(obj.interchangeableRectangles([[16,1],[13,7],[20,18],[21,15],[20,3],[18,12],[23,14],[16,14],[5,25],[3,8],[6,17],[22,10],[25,17],[8,13],[8,11],[4,14],[2,17],[9,22],[3,15],[18,1],[19,13],[26,6],[26,14],[9,10],[12,6],[24,3],[21,8],[17,6],[16,7],[8,9],[20,24],[25,26],[22,23],[4,25],[23,23],[24,8],[14,4],[10,18],[13,6],[7,6],[24,15],[16,22],[17,19],[2,16],[23,21],[15,26],[7,17],[14,7],[10,26],[9,8],[7,10],[1,1],[11,17],[4,20],[19,24],[18,24],[9,21],[20,22],[21,12],[10,23],[5,9],[2,3],[6,17],[5,20],[11,15],[7,19],[5,9],[12,13],[15,19],[3,26],[19,25],[13,6],[22,13],[18,7],[4,9],[13,24],[22,21],[21,9],[25,26],[21,20],[9,13],[10,5],[11,18],[6,20],[16,8]]))