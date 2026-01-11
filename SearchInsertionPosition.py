# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# pseudocode
# START
# GET nums and target
# START FOR LOOP  I STARTS FROM ZERO TO THE LAST INDEX OF nums
#     IF NUM[I] EQUAL TARGET 
#         RETURN  I
#     ELSE IF NUM[I] GREATER THAN TARGET
#         RETURN I-1
    
# IF LOOPS END WITHOUT BOTH CONDITION MET RETURN I+1

def SearchInsertion(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
             # that meen the element of the current index supposed to increase by one in indexing 
             # and the target takes its indexing number
            return i
    return i+1

nums = [1, 2, 5, 6]
target = 5
print(SearchInsertion(nums,target))
#output:2

nums = [1, 3, 5, 6]
target = 2
print(SearchInsertion(nums,target))
#output:1

nums = [1, 3, 5, 6]
target = 7
print(SearchInsertion(nums,target))
#output:4