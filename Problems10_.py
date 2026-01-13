#<! merge two sorted list !>


# pseudocode
# START
# CREATE SOTRTED LIST = []
# take two lists
# i goes from zero to len(list1) and j goes from zero to len(list2)
# start a while LOOP
#     WHILE I< length(list1) and j <list(2):
#         IF LIST[I] <= LIST[J]
#             APPEND THE LIST[I] TO SORTED LIST 
#             I = I+1
#         ELSE 
#             APPEND LIST[J] TO SORTED LIST
    

#     APPEND THE REMAINING ELEMENTS OF list1
#     APPEND THE REMAINING ELEMENTS OF list2


def MergeSortedList(list1, list2):
    sorted_list = []
    i=0
    j=0
    while i<len(list1) and j<len(list2):
        if list1[i]<=list2[j]:
            sorted_list.append(list1[i])
            i+=1
        else:
            sorted_list.append(list2[j])
            j +=1
    
    sorted_list.extend(list1[i:])
    sorted_list.extend(list2[j:])
    return sorted_list
list1 = [1,2,4]
list2 = [1,3,4]
print(MergeSortedList(list1,list2))
list1 = []
list2 = []
print(MergeSortedList(list1,list2))
list1 = []
list2 = [0]
print(MergeSortedList(list1,list2))