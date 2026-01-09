# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# pseudocode:
# START 
# TAKE haystack and needle
# I equal zero
# CREATE A LOOP
# the loop iterate until the element of haystack at which the length of the remaining element of haystack
# will be equal the length of needle or at the first occurance of needle in the haystack
# the function will Return the index of first occurance of needle in haystack or -1 if needle is not a part of haystack

def FirstOccurance(haystack, needle):
    i = 0
    while i <= len(haystack)-len(needle):
        if haystack[i:i+len(needle)] == needle:
            return i
        else:
            i+=1
    return -1


print(FirstOccurance("sadbutsad","sad"))
print(FirstOccurance("leetcode","leeto"))
# haystack = "sadbutsad"
# needle = "sad"
# i = 0
# print(haystack[i:i+len(needle)])