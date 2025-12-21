


def Palindrome(num):
    lst = list(map(int,str(num)))
    j= len(lst)-1

    for i in range(len(lst)):
        if i != j:
           if lst[i] == lst[j]:
                j = j-1 
           else:
                return False
        return True

x=242

print(Palindrome(x))