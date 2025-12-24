                        #psuodo-code 
                        #create a function that takes a list of strings as an input  
                        #convert each string into a seprate list of characters
                        #compare the length of each list of characters and find the smallest list
                        #shortest hold the smallest number of characters in a single list
                        #string_list hold the number of strings inside a list
                        #compare the first character of the smallest list to the other first character of the remaining lists
                        # if equal create a string and put the common character in it 
                        #repeat the process with the second character of the smallest list 
                        # keep repeating until you found non common character or reach the end of the smallest list 
                        # return a string with the common characters



def LongestCommonPrefix(strings_list):
    str_char_list = []
    common_prefix = []
    for i in range(len(strings_list)):
        str_char_list.append(list(strings_list[i]))
    
    
        shortest = min(str_char_list,key=len)
    
        same_order_char = [word[i] for word in strings_list] # get all the characters with the same order in strings  and put them in one list

        if len(set(same_order_char))== 1: # set remove all duplicates , if all characters are the same , the set will have exactly one element 
            common_prefix.append(same_order_char[0])
        else:
            break  # this will end as soon as one position doesnt match     

    
    return "".join(common_prefix)
    


print(LongestCommonPrefix(["abcd", "abyz", "abn"]))