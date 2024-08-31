
spells = [3,1,2]
potions = [1,2,3,4,5]
success = 7
result = []
potions.sort()
for i in range(len(spells)):
    if potions[len(potions)-1]*spells[i] <success:
        result.append(0)
        continue
    start = 0
    end = len(potions)
    mid=(start+end)//2
    while(start<end):
        if mid==0 or mid == len(potions) :
            break
        if potions[mid]*spells[i]>success or potions[mid]*spells[i] == success:
            end = mid-1
        else:
            start = mid+1

        mid = (start+end)//2
    if potions[mid]*spells[i] <success:
        mid+=1
    result.append(len(potions[mid:]))

print(result)