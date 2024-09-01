class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n==len(original):
            result = []
            i = 0
            for row in range(m):
                temp = []
                for col in range(n):
                    temp.append(original[i])
                    i+=1
                result.append(temp)
            return result
        else:
            return []


        