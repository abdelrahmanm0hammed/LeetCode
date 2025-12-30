# Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
#  The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# plain english:
# start 
# take an input list of sorted nums from the user 
# create a loop that iterate at a length of the sorted list -1
# compare the current element with the next element if equal remove the current element and move to the next element 
# if not equal move to the next element without deleting the current element 
# return the length of the list after the loop ends 

# pseudocode
# START 
# DEF A FUNCTION RemoveDuplicates takes a list 
#  I = 0
# WHILE I < len(list)-1
#     IF LIST[I] == LIST[I+1]:
#         REMOVE LIST[I]

#     ELSE
#         I = I +1
# RETURN length of list, list

def RemoveDuplicates(nums):
    i = 0
    while i <len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i+=1
    
    k = len(nums)
    return k , nums

print(RemoveDuplicates([1, 2, 2]))