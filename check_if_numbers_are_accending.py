class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        split_list = s.split()  #split and make the list of all the alphabet 
        result_list = [int(x) for x in split_list if x.isdigit()] #make the list of all the numbers
        print(result_list)
        if all(result_list[i]<result_list[i+1] for i in range(0,len(result_list)-1)) == True: #check the list is sorted or not
            return True
        else:
            return False
obj = Solution()
print(obj.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))