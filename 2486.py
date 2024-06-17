class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if len(t)>s:
            temp = s
            s = t
            t = temp
        #not solved
