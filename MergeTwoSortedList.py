#pseudocode
#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.




def MergeTwoSortedList(a, b):
    # i and j are pointers (indexes) for list a and list b
    i = j = 0

    # This list will store the final merged result
    linked_list = []

    # Loop while BOTH lists still have elements left to compare
    while i < len(a) and j < len(b):

        # Compare the current element from list a with list b
        if a[i] <= b[j]:
            # Add the smaller (or equal) element from list a to the result
            linked_list.append(a[i])

            # Move pointer i to the next element in list a
            i += 1
        else:
            # Add the smaller element from list b to the result
            linked_list.append(b[j])

            # Move pointer j to the next element in list b
            j += 1

    # Add any remaining elements from list a (if list b is finished)
    linked_list.extend(a[i:])

    # Add any remaining elements from list b (if list a is finished)
    linked_list.extend(b[j:])

    # Return the fully merged and sorted list
    return linked_list
