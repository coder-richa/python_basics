"""
    Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
    """
    
def isPalindrome(x: int) -> bool:
    # Return True for positive integers smaller than 10.
    if x >=0 and (x < 10):
        return True
    
    # Return false for integer with negative or multiple of 10 values.
    if x < 0 or (x !=0 and x % 10) == 0  :
        return False
    
        
    number = x
    # List to hold remainder
    rev = [] 
    while number > 0:
        rem  = number % 10
        number = number // 10
        rev.append(rem)
    
    # Compare reverse. 
    return rev == rev[-1::-1]

def main():
    print(isPalindrome(0))
    
if __name__ == '__main__':
    main()