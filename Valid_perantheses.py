#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

#solution psuedo code:
#create a function that takes a string as an arguement 
#create a loop that checks wheather the open bracket has an enclosing bracket next to it or corresponing to it in the same order
#example of s = "{}{}{[]}", "()[]{}"
def isValid(s: str) -> bool:
    # Create an empty stack to store opening brackets
    stack = []

    # Dictionary to match each closing bracket to its opening bracket
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Loop through each character in the string
    for char in s:

        # If the character is an opening bracket
        if char in matching.values():
            # Push the opening bracket onto the stack
            stack.append(char)

        # Otherwise, the character is a closing bracket
        else:
            # If the stack is empty, there is no opening bracket to match
            # OR the top of the stack does not match the closing bracket
            if not stack or stack[-1] != matching[char]:
                # The string is invalid
                return False

            # If it matches, remove the top opening bracket from the stack
            stack.pop()

    # After processing all characters:
    # If the stack is empty, all brackets were matched correctly
    # If not empty, there are unmatched opening brackets
    return not stack
