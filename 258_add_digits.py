class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        while True:
            result_sum = 0
            while num!=0:
                result_sum+=num%10
                num = int(num/10)
            num = result_sum
            if num<9:
                return num 