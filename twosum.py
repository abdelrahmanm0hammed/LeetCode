
#num = [1, 2, 3, 4, 5]
#print(len(num))

#for i in range(len(num)):
   
def sumTwo(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []   


print(sumTwo([2,7,11,15],9))

