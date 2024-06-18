class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty,profit)) # making a tuple to store the difficulty along with its profit 
        worker.sort() #sorting the work list to ensure the efficiency 
        i , max_profit ,result = 0,0,0 
        for ability in worker: #iterating through worker list
            while  i < len(jobs) and jobs[i][0]<=ability: #checking whether the end of the list and comparing that the difficulty is less thn to worker ability
                max_profit = max(max_profit,jobs[i][1])
                i+=1
            result+=max_profit
        return result
    