""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""




def is_valid_parantheses(s: str) -> bool:
    
    # Map to store opening and closing brackets mapping.
    dictionary = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Stack of parantheses.
    stack = []
    # Loop through the string.
    
    for char in s:
        
        # Check if the char is an opening parantheses
        if char == '(' or char == '{' or char == '[':
            # Push the char to the stack
            stack.append(char)
        
        # Check if the char is a closing parantheses
        else:
            
            # Check if the stack is empty
            if len(stack)==0:
                return False
       
            # Check if the last element in the stack is the same as the current character
            last_pushed_parantheses = stack.pop()
            if last_pushed_parantheses != dictionary[char]:
                return False    
            
    # Check if the stack is empty
    return len(stack) == 0


def main():
    test_cases = [
        {"input":"()","expected":True},
        {"input":"()[]{}","expected":True},
        {"input":"(]","expected":False},
    ]
    
    for test_case in test_cases:
        result = is_valid_parantheses(test_case['input'])
        status = result == test_case['expected']
        print(f" Pass: {status}  Input: {test_case['input']}  Output: {result}")
        
if __name__ == '__main__':
    main()