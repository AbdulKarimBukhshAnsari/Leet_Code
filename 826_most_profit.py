class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty,profit)) 
        worker.sort()
        i , max_profit ,result = 0,0,0
        for ability in worker:
            if i < len(jobs) and ability<=jobs[i][0]:
                max_profit = max(max_profit,jobs[i][1])
            i+=1
            result+=max_profit
        return result

