class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        for i in s:
            if len(result)==0 and i==" ":  #ignoring leading widespaces
                continue
            elif len(result)==0 and (i=="-" or i == "+"): #checking that if the first charcater is + or - if yes then append it into result
                result+=i
            elif i.isdigit() == True : #in each iteration if the digit is present append it 
                result+=i
            elif  i.isdigit() == False: # if character is other than + or - then simply break and terminate the loop because there is no need to chech further
                break
        if len(result)==1 and result.isdigit()==True:
            #if there is only one number in result then we check if there exits all number then we will convert into integer
            return int(result)
        if result[1:].isdigit()==True: #
            if int(result) > ((2**31)-1):
                return (2**31)-1
            elif int(result)<(-2**31):
                return -2**31
        else:
            return 0 
        if len(result) == 0:

            return 0
        if result[1:].isdigit()==True:
        
            return int(result)
obj = Solution()
print(obj.myAtoi(" -042"))   
#not solved


